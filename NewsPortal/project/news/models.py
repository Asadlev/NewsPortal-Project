from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(User, related_name='subscribed_categories')
