from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='dossiers.index'),
    url(r'dossiertest$', views.dossier, name='dossiers.dossiertest'),
    url(r'(?P<dossier_id>[0-9]+)$', views.testje, name='idk testje'),
]
