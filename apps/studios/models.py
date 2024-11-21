from django.db import models
from model_utils.models import UUIDModel

from apps.addresses.models import Address


class Studio(UUIDModel):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    capacity = models.IntegerField()
