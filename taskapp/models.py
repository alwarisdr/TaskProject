from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)