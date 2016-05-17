"""ViaSofie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import render_to_response
from django.template import RequestContext

from ViaSofie import settings
from . import views

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
      url(r'^password_change/$', auth_views.password_change, name='password_change'),
      url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),
      url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
      url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
      url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
          auth_views.password_reset_confirm, name='password_reset_confirm'),
      url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
      url(r'^admin/', admin.site.urls),
      url(r'^dossier/', include('dossiers.urls')),
      url(r'^panden/', include('panden.urls')),
      url(r'^gebruiker/', include('gebruikers.urls')),

      url(r'^$', views.index, name='index'),
      url(r'^about/$', views.about, name='ViaSofie.about'),
      url(r'^contact/$', views.contact, name='ViaSofie.contact'),
      url(r'^faq/$', views.faq, name='ViaSofie.faq'),
      url(r'^disclaimer/$', views.disclaimer, name='ViaSofie.disclaimer'),
      url(r'^privacy/$', views.privacy, name='ViaSofie.privacy'),
      url(r'^about/services/$', views.services, name='ViaSofie.services'),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
