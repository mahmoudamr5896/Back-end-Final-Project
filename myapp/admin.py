from django.contrib import admin

# Register your models here.
from myapp.models import Appointment, Doctor, Review

admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Review)
