from django.db import models
from django.db.models.fields import DateField

class Blog(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateField()