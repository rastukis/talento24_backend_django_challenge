import json
import hashlib

from django.core.cache import cache
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import UserSerializer
from constants.user import IDEM_KEY_USER
from constants.globals import IDEM_KEY, IDEM_KEY_REQUIRED, DETAIL_LBL, DUPLICATED_KEY, HttpLabels


class CustomPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        next_page = self.page.next_page_number() if self.page.has_next() else None
        previous_page = self.page.previous_page_number() if self.page.has_previous() else None

        return Response({
            "count": self.page.paginator.count,
            "total_pages": self.page.paginator.num_pages,
            "current_page": self.page.number,
            "next": next_page,
            "previous": previous_page,
            "results": data
        })


class UserCreateView(APIView):
    IDEMPOTENCY_TTL = 60 * 10

    def post(self, request):
        idempotency_key = request.headers.get(IDEM_KEY)

        if not idempotency_key:
            return Response(
                data={DETAIL_LBL: IDEM_KEY_REQUIRED},
                status=400
            )

        payload = json.dumps(request.data, sort_keys=True)
        payload_hash = hashlib.sha256(payload.encode()).hexdigest()

        redis_key = f"{IDEM_KEY_USER}{idempotency_key}"

        cached = cache.get(redis_key)

        if cached:
            cached_data = json.loads(cached)
            if cached_data[HttpLabels.PAYLOAD_HASH] != payload_hash:
                return Response(
                    data={DETAIL_LBL: DUPLICATED_KEY},
                    status=422
                )

            return Response(
                cached_data[HttpLabels.RESPONSE],
                status=cached_data[HttpLabels.STATUS]
            )

        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            with transaction.atomic():
                user = serializer.save()
                response_data = UserSerializer(user).data

                cache_payload = {
                    HttpLabels.PAYLOAD_HASH: payload_hash,
                    HttpLabels.RESPONSE: response_data,
                    HttpLabels.STATUS: 201,
                }

                cache.set(
                    redis_key,
                    json.dumps(cache_payload),
                    timeout=self.IDEMPOTENCY_TTL
                )

                return Response(
                    response_data,
                    status=201
                )
        except Exception as error:
            return Response(
                str(error),
                status=500
            )


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_fields = ["country"]

    search_fields = ["first_name", "last_name", "email"]
