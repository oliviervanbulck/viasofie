from django.contrib.auth.models import User
from django.db.models.functions import Concat
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from dal import autocomplete
from django.db.models import Value as V


# Create your views here.
from panden.models import Type


def index(request):
    context = {
    }
    return render(request, 'gebruikers/profile.html', context)


def login_user(request):
    redirect_url = '/'
    if request.POST:
        logout(request)
        username = password = ''
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.user.is_staff:
                    redirect_url = '/admin'
    return HttpResponseRedirect(redirect_url)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

