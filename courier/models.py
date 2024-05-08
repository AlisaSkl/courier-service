from django.contrib.auth.models import AbstractUser
from django.db import models

from courier_service import settings


class District(models.Model):
    name = models.CharField(max_length=255)
    courier = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="couriers"
    )

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name="restaurants"
    )

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Courier(AbstractUser):
    driving_license = models.CharField(max_length=9),

    class Meta:
        ordering = ("username", )
