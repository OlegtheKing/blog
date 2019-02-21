from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})  # returning a string which is url to that specific post

    # user.post_set is used to run queries on post objects related to that user, e.g
    # user.post_set.all() will return all posts related to that user or user.post_set.create()