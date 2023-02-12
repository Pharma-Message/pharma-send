from django.shortcuts import render, redirect

def chatpage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        context = {}
        return render(request, 'chat/chatpage.html')

# Create your views here.
