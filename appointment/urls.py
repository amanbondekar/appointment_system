from django.urls import path
from .views import doctor_booking

urlpatterns = [
    path('doctors/<int:doctor_id>/', doctor_booking, name='doctor_booking'),
]