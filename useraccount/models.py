from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_no = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    document = models.ImageField(upload_to='document')
    profile = models.ImageField(upload_to='profile',blank= True, null=True)

    def __str__(self):
        return self.username
    