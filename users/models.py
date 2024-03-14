from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username=models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=30,null=True,blank=True)

    

    def __str__(self):
        return self.email
    
   

  
