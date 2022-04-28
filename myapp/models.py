from django.db import models

class WordBank(models.Model):
    english = models.CharField(max_length=255)
    welsh = models.CharField(max_length=255)
