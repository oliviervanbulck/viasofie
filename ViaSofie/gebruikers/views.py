from django.contrib.auth.models import User
from django.db.models.functions import Concat
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from dal import autocomplete
from django.db.models import Value as V


# Create your views here.
from gebruikers.models import Woonplaats, Land
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


class WoonplaatsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Woonplaats.objects.none()

        if not self.request.user.is_superuser:
            return Woonplaats.objects.none()

        qs = Woonplaats.objects.all()

        if self.q:
            qs = qs.annotate(volledig=Concat('postcode', V(' '), 'gemeente')).filter(volledig__icontains=self.q)

        return qs


class LandAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Land.objects.none()

        if not self.request.user.is_superuser:
            return Land.objects.none()

        qs = Land.objects.all()

        if self.q:
            qs = qs.annotate(volledig=Concat('landcode', V(' '), 'naam')).filter(volledig__icontains=self.q)

        return qs
