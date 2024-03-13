from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Doctor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
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