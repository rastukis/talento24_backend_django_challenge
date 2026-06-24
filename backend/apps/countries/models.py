from django.db import models


class Country(models.Model):
    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.iso} - {self.name}"
