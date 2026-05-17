from django.contrib.auth.models import User
from django.db import models

from config.choices import ModelChoices
from mixins.models import BaseModel


class Organization(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Membership(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey("users.Organization", on_delete=models.CASCADE)
    role = models.CharField(
        choices=ModelChoices.ROLE_CHOICES,
        default=ModelChoices.ROLE_DEFAULT,
        max_length=10,
    )
