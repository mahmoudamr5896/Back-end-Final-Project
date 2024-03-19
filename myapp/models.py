from datetime import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role=models.CharField(null=True, blank= True)
    

    def _str_(self):
        return self.username
    
class Doctor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    username = models.CharField(unique=True, max_length=100, blank=True, null=True)  # Assuming username is unique
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True)
    experience = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    @property
    def user(self):
        return CustomUser.objects.get(username=self.username)
    
    def generate_availability(self):
        # Implement logic to generate availability
        # For example, you might query appointments for this doctor
        # and return a list of available time slots
        current_time = timezone.now()
        # Example logic to return available time slots for the next week
        available_slots = []
        for i in range(7):
            date = current_time + timezone.timedelta(days=i)
            # Check if the doctor is available on this date and time
            # If available, add it to available_slots list
            available_slots.append(date)
        return available_slots
    
class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    username = models.CharField(unique=True,max_length=100,blank=True, null=True)  # Assuming username is unique
    name=models.CharField(max_length=100,blank=True, null=True)
    image=models.ImageField(upload_to='img',null=True,blank=True)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    medical_history = models.TextField()

    @property
    def user(self):
        return CustomUser.objects.get(username=self.username)
    
    def __str__(self):
        return self.name
    from django.core.validators import MinValueValidator, MaxValueValidator



class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True,blank=True)
    date_time = models.CharField()  
    problems = models.TextField()  
    status = models.BooleanField(default=False) 
    Reasone_reject=models.CharField(max_length=50,blank=True, null=True) 

    def __str__(self):
        return f"Appointment at {self.date_time} - {self.status}"
    


class Review(models.Model):
   
    Doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=True)
    User_id = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True,blank=True)

    Review = models.TextField()
    Rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Availability(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,blank=True, null=True)
    day = models.CharField(max_length=10, choices=DAY_CHOICES,blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.doctor.name} - {self.day} - {self.start_time} to {self.end_time}"