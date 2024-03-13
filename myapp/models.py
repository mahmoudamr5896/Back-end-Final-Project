from django.db import models
#viewset
# Create your models here.
from django.db import models

class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    repeat_password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    medical_history = models.TextField()

    def __str__(self):
        return f"Patient {self.id}"
