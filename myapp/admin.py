from django.contrib import admin

# Register your models here.
from myapp.models import Appointment, Doctor, Review, Patient

admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(Patient)
