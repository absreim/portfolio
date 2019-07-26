from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()
