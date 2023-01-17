from django import forms
from pharmasend.models import Doctor
from django.forms import ModelForm

ACC_TYPE = [
    ("doctor", "Doctor"),
    ("pharmacist", "Pharmacist"),
    ("hospadmin", "Hospital Admin")
]

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['fname', 'lname', 'uname', 'email', 'pwd']
