from django.contrib import admin

# Register your models here.
from panden.models import Pand, Type, Kenmerk, PandImmoLink, Foto, PandKenmerkPerPand

admin.site.register(Pand)
admin.site.register(Type)
admin.site.register(Kenmerk)
admin.site.register(PandImmoLink)
admin.site.register(Foto)
admin.site.register(PandKenmerkPerPand)
