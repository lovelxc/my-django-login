from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
