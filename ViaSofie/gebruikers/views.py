from django.db.models.functions import Concat
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from dal import autocomplete
from django.db.models import Value as V

from gebruikers.models import Woonplaats, Land


def index(request):
    context = {
    }
    return render(request, 'gebruikers/profile.html', context)


def login_user(request):
    redirect_url = reverse('index')
    if request.POST:
        logout(request)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.user.is_staff:
                    redirect_url = reverse('admin:index')
            else:
                redirect_url += '?le=2'
        else:
            redirect_url += '?le=1'
    return redirect(redirect_url)


def logout_user(request):
    logout(request)
    return redirect('index')


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
