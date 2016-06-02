from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

admin.autodiscover()  # Zonder autodiscover vindt Django het geregistreerde model niet!
admin.site.unregister(Site)  # Dit model moet niet in het admin panel verschijnen
admin.site.unregister(Group)
