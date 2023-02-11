from django import forms
from django.contrib.auth.forms import UserCreationForm
<<<<<<< Updated upstream
from accountforms.models import Doctor, Pharmacist, Account
=======
from accountforms.models import Doctor, Pharmacist, Account, Order
>>>>>>> Stashed changes
from django.forms import ModelForm, TextInput, CharField, Form
from django.db import models

ACC_TYPE = [
    ("doctor", "Doctor"),
    ("pharmacist", "Pharmacist"),
    ("hospadmin", "Hospital Admin")
]

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
<<<<<<< Updated upstream
        fields = ['fname', 'lname', 'uname', 'email', 'pwd']
=======
        fields = ['name', 'doctorid', 'email']
>>>>>>> Stashed changes
    
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        for k in self.fields:
            if (issubclass(type(self.fields[k]), CharField)):
                self.fields[k].widget.attrs.update({'class': 'form_input'})
                self.fields[k].widget.attrs.update({'placeholder': k})
<<<<<<< Updated upstream
                pass
            self.fields['pwd'].widget.input_type = 'password'
=======
        self.fields['doctorid'].label = "Doctor ID"
>>>>>>> Stashed changes


class PharmacistForm(ModelForm):
    class Meta:
        model = Pharmacist
<<<<<<< Updated upstream
        fields = ['fname', 'lname', 'uname', 'clinic', 'email', 'pwd']
=======
        fields = ['clinic', 'name', 'email']
>>>>>>> Stashed changes
    
    def __init__(self, *args, **kwargs):
        super(PharmacistForm, self).__init__(*args, **kwargs)
        for k in self.fields:
            if (issubclass(type(self.fields[k]), CharField)):
                self.fields[k].widget.attrs.update({'class': 'form_input'})
                self.fields[k].widget.attrs.update({'placeholder': k})
<<<<<<< Updated upstream
            self.fields['pwd'].widget.input_type = 'password'
=======

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['reciever', 'message', 'patientid']
    
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for k in self.fields:
            if (issubclass(type(self.fields[k]), CharField)):
                self.fields[k].widget.attrs.update({'class': 'form_input'})
                self.fields[k].widget.attrs.update({'placeholder': k})

>>>>>>> Stashed changes

class AccForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username']
    def __init__(self, *args, **kwargs):
        super(AccForm, self).__init__(*args, **kwargs)
        for k in self.fields:
            if (issubclass(type(self.fields[k]), CharField)):
                self.fields[k].widget.attrs.update({'class': 'form_input'})
                self.fields[k].widget.attrs.update({'placeholder': k})
            #self.fields['password'].widget.input_type = 'password'

<<<<<<< Updated upstream
class AuthForm(forms.Form):
    email = forms.CharField(max_length=60)
    password = forms.CharField(max_length=255)
=======

class AuthForm(forms.Form):
    email = forms.CharField(max_length=60)
    password = forms.CharField(max_length=255)
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        for k in self.fields:
            if (issubclass(type(self.fields[k]), CharField)):
                self.fields[k].widget.attrs.update({'class': 'form_input'})
                self.fields[k].widget.attrs.update({'placeholder': k})
        self.fields['password'].widget.input_type = 'password'
        self.fields['email'].label = "eMail"
>>>>>>> Stashed changes


    #def __init__(self, *args, **kwargs):
    #    super(AuthForm, self).__init__(*args, **kwargs)
    #    print(self.fields.keys()) 
        #self.fields['password'].widget.input_type = 'password'