from django.contrib.auth.models import User
from django.db import models

from config.choices import ModelChoices
from mixins.models import BaseModel


class Project(BaseModel):
    organization = models.ForeignKey("users.Organization", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(BaseModel):
    project = models.ForeignKey("core.Project", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=15,
        default=ModelChoices.TASK_STATUS_DEFAULT,
        choices=ModelChoices.TASK_STATUS_CHOICES,
    )
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title
