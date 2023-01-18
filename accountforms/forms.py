from django import forms
from accountforms.models import Doctor, Pharmacist
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
    
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        for k in self.fields:
            if (self.fields[k].input_type == 'text'):
                self.fields[k].widget.attrs.update({'class': 'textboxinput'})


class PharmacistForm(ModelForm):
    class Meta:
        model = Pharmacist
        fields = ['fname', 'lname', 'uname', 'clinic', 'email', 'pwd']
