from django.contrib.auth.models import AbstractUser
from django.db import models

from courier_service import settings


class District(models.Model):
    name = models.CharField(max_length=255)
    couriers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="districts"
    )

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=255, blank=True)
    address = models.TextField()
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
    driving_license = models.CharField(max_length=9, default="Unknown")
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ("username", )
