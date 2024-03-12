from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Appointment(models.Model):
    date_time = models.DateTimeField()  
    problems = models.TextField()  
    status = models.BooleanField(default=False)  

    def __str__(self):
        return f"Appointment at {self.date_time} - {self.status}"
    





class Review(models.Model):
    review_comment = models.TextField()
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


    
