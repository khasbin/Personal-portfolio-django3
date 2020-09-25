from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    description = models.TextField(max_length = 5000)


