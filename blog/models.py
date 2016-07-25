from django.db import models

# Create your models here.
class BlogPost(models.Model) :
    title = models.CharField(max_length = 128)
    abstract = models.TextField(blank = True)
    body = models.TextField()
    timestamp = models.DateTimeField()
    tags = models.CharField(max_length = 256, blank = True)
