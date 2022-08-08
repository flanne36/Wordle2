from django.db import models

# Create your models here.
class Wordsdata(models.Model):
    words = models.TextField(null=True)