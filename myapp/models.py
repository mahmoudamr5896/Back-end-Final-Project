from django.db import models
#viewset
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser):
    role = models.CharField(max_length=100, null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.username
    
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


class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100 , null=True,blank=True)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    medical_history = models.TextField()

    def _str_(self):
        return f"Patient {self.id}"
    

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True,blank=True)
    date_time = models.DateTimeField()  
    problems = models.TextField()  
    status = models.BooleanField(default=False)  

    def __str__(self):
        return f"Appointment at {self.date_time} - {self.status}"
    


class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    review_comment = models.TextField()
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Review by {self.patient} for {self.doctor}"