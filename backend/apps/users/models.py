from django.db import models

from apps.countries.models import Country


class User(models.Model):
    first_name = models.CharField(max_length=90, null=False)
    last_name = models.CharField(max_length=120, null=False)
    email = models.EmailField(null=False)
    age = models.SmallIntegerField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

