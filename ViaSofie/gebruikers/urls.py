from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='gebruikers.index'),
    url(r'^login/$', views.login_user, name='gebruikers.login'),
    url(r'^logout/$', views.logout_user, name='gebruikers.logout'),
]
