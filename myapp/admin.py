from django.contrib import admin

# Register your models here.
from myapp.models import *

admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(Patient)
admin.site.register(Payment)
admin.site.register(Availability)
