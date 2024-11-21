from django.db import models
from model_utils.models import UUIDModel, SoftDeletableModel, TimeStampedModel


# Create your models here.


class Address(UUIDModel, TimeStampedModel, SoftDeletableModel):
    address = models.CharField(max_length=256)
