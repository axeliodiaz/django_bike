from django.contrib.auth.models import AbstractUser
from model_utils.models import UUIDModel, SoftDeletableModel, TimeStampedModel


class User(AbstractUser, UUIDModel, SoftDeletableModel, TimeStampedModel):
    pass
