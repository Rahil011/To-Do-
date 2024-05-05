from django.db import models

# Create your models here.

class reminder(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
