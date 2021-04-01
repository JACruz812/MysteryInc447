from django.db import models


class Story(models.Model):
    details = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='evidence')
    parent_clue = models.CharField(max_length=100)
