"""
URL configuration for backend_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import CustomUserViewSet, DoctorViewSet, AppointmentViewSet, PatientViewSet, ReviewFunBaseView
from users.views import UserViewSet, AuthViewSet
from myapp.views import AvailabilityViewSet
from myapp.views import DoctorAvailabilityView

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'appointments', AppointmentViewSet, basename='appointments')
router.register(r'reviews-all', ReviewFunBaseView, basename='reviews-all')
router.register(r'patients', PatientViewSet)
router.register(r'users', UserViewSet, basename='user')
router.register(r'availabilities', AvailabilityViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
path('doctors/<int:doctor_id>/availability/', DoctorAvailabilityView.as_view(), name='doctor_availability'),

]+ router.urls

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)