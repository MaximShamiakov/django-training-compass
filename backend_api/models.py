from django.db import models
from django.contrib.auth.models import User


class Material(models.Model):
    title = models.CharField(max_length=255, default='')
    question = models.TextField(default='')
    answer = models.TextField(default='')

    def __str__(self) -> str:
        return self.question


class Сategories(models.Model):
    category = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')

    def __str__(self) -> str:
        return self.title


class ProjectInformation(models.Model):
    title = models.CharField(max_length=255, default='')
    body = models.TextField(default='')

    def __str__(self) -> str:
        return self.title
