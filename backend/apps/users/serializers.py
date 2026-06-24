from rest_framework import serializers

from apps.countries.serializer import CountrySerializer
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    country_data = CountrySerializer(source="country", read_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "age", "country", "country_data"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "country": {"write_only": True}
        }

