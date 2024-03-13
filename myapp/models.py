from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Doctor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    image=models.ImageField(blank=True,null=True)
    experience = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=True)
    date_time = models.DateTimeField()  
    problems = models.TextField()  
    status = models.BooleanField(default=False)  

    def __str__(self):
        return f"Appointment at {self.date_time} - {self.status}"
    


class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=True)
    review_comment = models.TextField()
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role=models.CharField(null=True, blank= True)
    

    def _str_(self):
        return self.username
    
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    medical_history = models.TextField()
    

    def _str_(self):
        return f"Patient {self.id}"
from django.core.validators import MinValueValidator, MaxValueValidator