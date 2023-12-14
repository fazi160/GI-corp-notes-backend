from django.db import models

# Create your models here.

# model for Notes
class Notes(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
