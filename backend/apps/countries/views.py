from rest_framework.generics import ListAPIView

from apps.countries.models import Country
from apps.countries.serializer import CountrySerializer


class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
