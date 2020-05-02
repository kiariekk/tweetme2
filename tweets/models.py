"""Django models module import"""
from django.db import models


class Tweet(models.Model):
    """Creates a model for posting Tweets"""
    # Maps to SQL data
    # id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
