from django.db import models

# Create your models here.
class Appointment(models.Model):
    date_time = models.DateTimeField()  
    problems = models.TextField()  
    status = models.BooleanField(default=False)  

    def __str__(self):
        return f"Appointment at {self.date_time} - {self.status}"