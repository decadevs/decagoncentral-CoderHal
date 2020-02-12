from django.db import models

# Create your models here.

class UserModel(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname
