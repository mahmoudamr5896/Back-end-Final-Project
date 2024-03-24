from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from myapp.models import Appointment, Availability, Doctor, Patient, Payment, Review

=======
from myapp.models import Appointment, Doctor, Review, Patient
>>>>>>> 541dadc4d8dc8e1cc4898b49f7501654739e2919

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Review)
<<<<<<< HEAD
admin.site.register(Availability)



=======
admin.site.register(Patient)
>>>>>>> 541dadc4d8dc8e1cc4898b49f7501654739e2919
