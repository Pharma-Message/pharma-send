from pharmasend.forms import DoctorForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def doctor_create(request: HttpRequest):
    form = DoctorForm()
    if (request.method == 'POST'):
        form = DoctorForm(request.POST)
        if (form.is_valid()):
            form.save()
    return render(request, "registration/doctor_registration.html", {'form': form})

def pharmacist_create(request: HttpRequest):
    form = DoctorForm()
    if (request.method == 'POST'):
        form = DoctorForm(request.POST)
        if (form.is_valid()):
            form.save()
    return render(request, "registration/doctor_registration.html", {'form': form})

def hospital_create(request: HttpRequest):
    form = DoctorForm()
    if (request.method == 'POST'):
        form = DoctorForm(request.POST)
        if (form.is_valid()):
            form.save()
    return render(request, "registration/doctor_registration.html", {'form': form})