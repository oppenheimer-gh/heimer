from django.db import models

from common.base_model import BaseModel
from post.models import Post
from user.models import User


class Comment(BaseModel):
    message = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
