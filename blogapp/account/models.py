from django.db import models

# Create your models here.
class UserJob(models.Model):
    username = models.CharField(max_length=100, editable=False)
    job = models.CharField(max_length=100, editable=False)