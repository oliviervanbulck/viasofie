from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'gebruikers/login.html', context)


def login_user(request):
    if request.POST:
        username = password = ''
        #logout(request)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/gebruiker')
    return HttpResponseRedirect('/')
    #return render(request, 'gebruikers/login.html', context=RequestContext(request))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/gebruiker')
