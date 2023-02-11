from django.shortcuts import render

# Create your views here.
from accountforms.forms import DoctorForm, PharmacistForm, AuthForm, AccForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from accountforms.models import Pharmacist, AccountManager, Account
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize
from accountforms.backends import CIModelBackend

def doctor_create(request: HttpRequest):
    form = DoctorForm()
    if (request.method == 'POST'):
        form = DoctorForm(request.POST)
        if (form.is_valid()):
            form.save()
        form = DoctorForm()
    return render(request, "registration/doctor_registration.html", {'form': form})

def pharmacist_create(request: HttpRequest):
    print(Pharmacist.objects.all().filter(fname__exact="asdf"))
    form = PharmacistForm()
    if (request.method == 'POST'):
        form = PharmacistForm(request.POST)
        if (form.is_valid()):
            qs = Account.objects.all().filter(email=form.data['email'])
            print(qs)
            print(form.data['email'])
            if (qs.exists()):
                #pharmacist = form.save()
                user = qs.get(email=form.data['email'])
                print("usertype is ", type(user))
                
        form = DoctorForm()
    return render(request, "registration/pharmacist_registration.html", {'form': form})

def hospital_create(request: HttpRequest):
    form = DoctorForm()
    if (request.method == 'POST'):
        form = DoctorForm(request.POST)
        if (form.is_valid()):
            form.save()
    return render(request, "registration/doctor_registration.html", {'form': form})

def acc_create(request: HttpRequest):
    form = AccForm()
    if (request.method == 'POST'):
        form = AccForm(data=request.POST)
        print(request.session.get('user'))
        print(form.data)
        print("login", request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
            
        print("vlid", form.is_valid())
        if (form.is_valid()):
            print("WOOOOOO")
            user = form.save(commit=True)
            print("saved user")
            login(request, user, backend="accountforms.backends.CIModelBackend")
        
        return render(request, "home.html")
    return render(request, "registration/acc_registration.html", {'form': form})


def login_view(request: HttpRequest):
    form = AuthForm()
    if (request.method == 'POST'):
        form = AuthForm(request.POST)
        print(request.session.get('user'))
        print(form.data)
        print("login", request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        print( form.data.keys() )
            
        print(form.is_valid())
        if (form.is_valid()):
            email = form.data['email']
            password = form.data['password']
            user = authenticate(username=email, password=password)
            print(user)
            login(request, user, backend="accountforms.backends.CIModelBackend")
            return render(request, "home.html", {})
    return render(request, "registration/login.html", {'form': form})

def logout_view(request: HttpRequest):
    logout(request)
    print(request.POST)
    print("logout", request.session.get('user'))
    return render(request, "home.html", {})

def account_view(request: HttpRequest):
    if (request.user.is_authenticated):
        return render(request, "registration/acc.html")
    else:
        return render(request, "home.html")
    
