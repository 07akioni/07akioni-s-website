from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_(request) :
    context = {}
    return render(request, 'login.html', context)

def register(request) :
    context = {}
    return render(request, 'register.html', context)

def verify(request) :
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
            # Redirect to a success page.
        else:
            return HttpResponse('disabled account...')
            # Return a 'disabled account' error message
            ...
    else:
        return HttpResponse('invalid login...')
        # Return an 'invalid login' error message.

def newuser(request) :
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, 'youdontneed@email.com', password)
    user.save()
    return HttpResponseRedirect('/auth/login/')


def logout_(request) :
    logout(request)
    return HttpResponseRedirect('/')
