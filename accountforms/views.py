from django.shortcuts import render

# Create your views here.
from accountforms.forms import DoctorForm, PharmacistForm
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
    form = PharmacistForm()
    form.auto_id 
    if (request.method == 'POST'):
        form = PharmacistForm(request.POST)
        if (form.is_valid()):
            form.save()
    else:
        print(form)
    return render(request, "registration/pharmacist_registration.html", {'form': form})

def hospital_create(request: HttpRequest):
    form = DoctorForm()
    if (request.method == 'POST'):
        form = DoctorForm(request.POST)
        if (form.is_valid()):
            form.save()
    return render(request, "registration/doctor_registration.html", {'form': form})