from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Doctor, Slot, Appointment

@login_required
def doctor_booking(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    slots = Slot.objects.filter(doctor=doctor, date__gte=timezone.now().date(), is_booked=False)

    if request.method == 'POST':
        user_email = request.user.email
        user_otp = request.POST['otp']

        # Authenticating user
        user = authenticate(request, username=user_email, password=user_otp)

        if user is not None:
            # User authenticated, handle appointment booking
            slot_id = request.POST.get('slot_id')
            slot = get_object_or_404(Slot, pk=slot_id)
            appointment = Appointment(slot=slot, user=user, is_booked=True)
            appointment.save()

            return HttpResponse('Appointment booked successfully!')
        else:
            return HttpResponse('Authentication failed. Please check your email and OTP.')

    context = {
        'doctor': doctor,
        'slots': slots,
    }

    return render(request, 'appointment_system/booking_page.html', context)
