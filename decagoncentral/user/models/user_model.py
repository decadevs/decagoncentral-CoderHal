from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_Length=100)
    username = models.CharField(max_Length=30)
    password = models.CharField(max_Length=100)
    email = models.EmailField()
    Position = models.CharField(mx_Length=100)

    def __str__(self):
        return self.fullname
