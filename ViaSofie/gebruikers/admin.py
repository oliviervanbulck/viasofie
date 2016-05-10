from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from django_mongoengine.mongo_auth.models import MongoUser
from models import Gebruiker, Land, Adres


# Register your models here.
class GebruikerInline(admin.StackedInline):
    model = Gebruiker
    can_delete = False
    verbose_name_plural = 'gebruiker'


# Define a new User admin
class UserAdmin(admin.ModelAdmin):
    inlines = (GebruikerInline, )


# Basis ModelAdmin voor AdminModel objecten die niet zichtbaar mogen zijn op indexpagina van adminpaneel.
class HiddenAdminModel(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class LandAdmin(HiddenAdminModel):
    pass


class AdresAdmin(HiddenAdminModel):
    pass


# Re-register UserAdmin
# admin.site.unregister(MongoUser)
admin.site.register(MongoUser, UserAdmin)
admin.site.register(Land, LandAdmin)
admin.site.register(Adres, AdresAdmin)
