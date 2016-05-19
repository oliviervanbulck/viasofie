from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='panden.index'),
    url(r'^kopen/$', views.index, name='panden.kopen'),
    url(r'^huren/$', views.huren, name='panden.huren'),
    url(r'^(?P<pand_id>[0-9]+)$', views.pand_detail, name='panden.detail'),
]
