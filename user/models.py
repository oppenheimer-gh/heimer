import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from safedelete import SOFT_DELETE_CASCADE

from common.base_model import BaseModel
from user.managers import UserManager


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    profile_photo_url = models.TextField(default="")
    first_name = None
    last_name = None
    email = models.EmailField(blank=False, null=False)
    is_mentor = models.BooleanField(blank=False, null=False)

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username


class Mentor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mentor")
    is_available = models.BooleanField(default=True)

    _safedelete_policy = SOFT_DELETE_CASCADE

    @property
    def get_mentees(self):
        return Mentee.objects.filter(mentor=self)

    def __str__(self):
        return self.user.username


class Mentee(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mentee")
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True)

    _safedelete_policy = SOFT_DELETE_CASCADE

    def __str__(self):
        return self.user.username
