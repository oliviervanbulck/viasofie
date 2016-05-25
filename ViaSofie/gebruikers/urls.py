from django.conf.urls import url

from gebruikers import views as gviews
from gebruikers.views import WoonplaatsAutocomplete, LandAutocomplete
from . import views

urlpatterns = [
    url(r'^$', views.index, name='gebruikers.index'),
    url(r'^login/$', views.login_user, name='gebruikers.login'),
    url(r'^logout/$', views.logout_user, name='gebruikers.logout'),
    url(
        r'^woonplaats-autocomplete/$',
        WoonplaatsAutocomplete.as_view(),
        name='woonplaats-autocomplete',
    ),
    url(
        r'^land-autocomplete/$',
        LandAutocomplete.as_view(),
        name='land-autocomplete',
    ),
]
