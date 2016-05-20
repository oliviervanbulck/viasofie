from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='dossiers.index'),
    url(r'(?P<dossier_id>[0-9]+)$', views.dossier, name='dossiers.dossier'),
]
