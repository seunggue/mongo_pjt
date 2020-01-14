from django.db import models

# Create your models here.

class Partner(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    duedate = models.DateField()
    password = models.IntegerField()
    