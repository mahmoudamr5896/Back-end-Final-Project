from django.contrib import admin

# Register your models here.
from myapp.models import Appointment,  Review

admin.site.register(Appointment)


admin.site.register(Review)