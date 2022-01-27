from django.db import models
from django.contrib.auth.models import AbstractUser

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
)

VIDEO_TYPE = (('sports', 'Sports'),
              ('gaming', 'Gaming'),
              ('live', 'Live'),
              ('premium', 'Premium'),
              ('fashion', 'Fashion'),
              ('beauty', 'Beauty'),
              ('learning', 'Learning'),
              ('movies', 'Movies'),
              ('shows', 'Shows'),
              ('news', 'News'),
              ('other', 'Other'),
              )


class User(AbstractUser):
    profiles = models.ManyToManyField('Profile')


class Profile(models.Model):
    name = models.CharField(max_length=225)
    email = models.TextField(max_length=225)
    age_limit = models.CharField(max_length=5, choices=AGE_CHOICES)
    subscriptions = models.ManyToManyField('Channel')

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    videos = models.ManyToManyField('Video')


class Video(models.Model):
    title: str = models.CharField(max_length=225)
    description: str = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=VIDEO_TYPE)
    videos = models.ManyToManyField('Video')
    age_limit = models.CharField(
        max_length=5, choices=AGE_CHOICES, blank=True, null=True)
