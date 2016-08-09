from django.db import models

# Create your models here.
class Comment(models.Model) :
    body = models.TextField()
    timestamp = models.DateTimeField()
    username = models.CharField(max_length = 200)
