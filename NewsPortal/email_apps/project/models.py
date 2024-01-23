from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Appointment(models.Model):
    date = models.DateTimeField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=29,
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'


class Post(models.Model):
    # ваша текущая модель
    content_summary = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(User, related_name='subscribed_categories')


