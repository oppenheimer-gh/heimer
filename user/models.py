import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from user.managers import UserManager


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=255, unique=True)
    profile_photo_url = models.TextField(default="")
    first_name = None
    last_name = None
    email = None

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username
