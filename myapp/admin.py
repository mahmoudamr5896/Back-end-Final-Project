from django.contrib import admin

# Register your models here.
from myapp.models import Appointment, Availability, Doctor, Patient, Payment, Review


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Availability)



