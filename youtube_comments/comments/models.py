from django.db import models
import datetime

# Create your models here.

class Comment(models.Model):
    comment_text = models.CharField(max_length=250)
    parent = models.ForeignKey('Comment', default=None, blank=True, null=True, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    video = models.CharField(max_length=50)

