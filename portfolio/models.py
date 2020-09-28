from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = 'portfolio/images/')
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length = 200)

    def __str__(self):
        return self.name


