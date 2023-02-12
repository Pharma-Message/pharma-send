from django.shortcuts import render

# Create your views here.
from accountforms.forms import OrderForm, DoctorForm, PharmacistForm, AuthForm, AccForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from accountforms.models import Pharmacist, Account
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize
from accountforms.backends import CIModelBackend
from django.contrib.sessions.models import Session

def doctor_create(request: HttpRequest):
    form = DoctorForm()
    form.fields.pop('email')
    if (request.method == 'POST'):
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        email = session_data["_auth_user_id"]

        form = DoctorForm(request.POST)
        form.data = form.data.copy()
        form.data['email'] = email
        if (form.is_valid()):
            if (Account.objects.all().filter(email__exact=email).exists()):
                print(email)
                print(form.data)
                d = form.save()

                acc = Account.objects.get(email__exact=email)
                acc.duser = d
                acc.save()
        return render(request, "registration/acc.html")
    return render(request, "registration/doctor_registration.html", {'form': form})

def pharmacist_create(request: HttpRequest):
    form = PharmacistForm()
    form.fields.pop('email')
    if (request.method == 'POST'):
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        email = session_data["_auth_user_id"]

        form = PharmacistForm(request.POST)
        form.data = form.data.copy()
        form.data['email'] = email
        if (form.is_valid()):
            if (Account.objects.all().filter(email__exact=email).exists()):
                p = form.save()

                acc = Account.objects.get(email__exact=email)
                acc.puser = p
                acc.save()
        return render(request, "registration/acc.html")
    
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
            
        if (form.is_valid()):
            login(request, form.save(), backend="accountforms.backends.CIModelBackend")
        
        return render(request, "home.html")
    return render(request, "registration/acc_registration.html", {'form': form})


def login_view(request: HttpRequest):
    print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
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
            if (user == None):
                return render(request, "registration/login.html", {'form': form, 'warning': 'Password or username is incorrect'})

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
        dat = {}
        print(request.user.puser)
        if (request.user.puser != None):
            dat["puser"] = True
        if (request.user.duser != None):
            dat["duser"] = True
        return render(request, "registration/acc.html", dat)
    else:
        return redirect("home")
    
def register_view(request: HttpRequest):
    dat = {}
    if (request.user.is_authenticated):
        print(request.user.puser)
        if (request.user.puser != None):
            dat["puser"] = True
        if (request.user.duser != None):
            dat["duser"] = True

    return render(request, "registration/registration.html", dat)

def send_order_view(request: HttpRequest):
    if (request.user.is_authenticated):
        if (request.user.duser != None):
            form = OrderForm()
            if (request.method == "POST"):
                form = OrderForm(request.POST)
                session = Session.objects.get(session_key=request.session.session_key)
                session_data = session.get_decoded()
                email = session_data["_auth_user_id"]
                if (form.is_valid()):
                    form.data = form.data.copy()
                    form.data['sender'] = email
                    acc = Account.objects.get(email__exact=form.data['reciever'])
                    if (acc.puser != None):
                        form.save()
                    else:
                        return render(request, "registration/send.html", {'form': form, 'warning': 'Sender account not found'})
                return account_view(request)
            else:
                return render(request, "messages/send.html", {'form': form})
        else: 
            return account_view(request)
    else:
        return render(request, "registration/login.html")
