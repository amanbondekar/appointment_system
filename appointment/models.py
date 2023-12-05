from django.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

class Slot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class Appointment(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    user_email = models.EmailField()
    user_otp = models.CharField(max_length=6)
    is_booked = models.BooleanField(default=False)
