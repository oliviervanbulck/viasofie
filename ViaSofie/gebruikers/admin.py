from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.core.validators import EmailValidator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.translation import ugettext, ugettext_lazy as _

from gebruikers.forms import GebruikerForm, AdresForm
from models import Gebruiker, Land, Adres, Woonplaats


# Register your models here.


# Inline voor adminpaneel => Gebruiker in User
class GebruikerInline(admin.StackedInline):
    model = Gebruiker
    form = GebruikerForm
    can_delete = False
    verbose_name_plural = 'gebruiker'


# Oplossing voor e-mailadres als username te gebruiken
User._meta.get_field('username').max_length = 255  # Set max length of username to higher number
User._meta.get_field('username').help_text = None  # Change help text for username
User._meta.get_field('username').default_validators = []  # Remove basic validators
User._meta.get_field('username').validators = []  # Remove basic validators
User._meta.get_field('username').verbose_name = 'E-mailadres'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (GebruikerInline, )
    exclude = ('email',)
    actions = ('set_admin', 'set_active', 'set_inactive',)
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active',)
    # _and_fieldsets = ()

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("user_permissions", "email",)
        # Dynamically overriding
        # self.fieldsets[2][1]["fields"] = ('is_active', 'is_staff', 'is_superuser', 'groups')
        self.fieldsets = (
            (None, {'fields': ('username', 'password')}),
            (_('Personal info'), {'fields': ('first_name', 'last_name')}),  # removed email from this tuple
            (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                           'groups')}),  # removed user_permissions from this tuple
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        return form

    def set_admin(self, request, queryset):
        queryset.update(is_staff=True, is_superuser=True)
        group = Group.objects.get(name="Makelaar")
        for user in queryset:
            group.user_set.add(user)

    set_admin.short_description = 'Geef gebruikers adminrechten'

    def set_active(self, request, queryset):
        queryset.update(is_active=True)

    set_active.short_description = 'Maak gebruikers actief'

    def set_inactive(self, request, queryset):
        queryset.update(is_active=False)

    set_inactive.short_description = 'Maak gebruikers inactief'


# Basis ModelAdmin voor AdminModel objecten die niet zichtbaar mogen zijn op indexpagina van adminpaneel.
class HiddenAdminModel(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


# Land niet zichtbaar in adminpaneel
class LandAdmin(HiddenAdminModel):
    pass


# Adres niet zichtbaar in adminpaneel en opties toegepast
class AdresAdmin(HiddenAdminModel):
    form = AdresForm
    list_per_page = 25


# Oplossing om e-mail als username te kunnen gebruiken
def _user_clean(user):
    """
    Require the value of `username` to be an email. The `email` field
    then adopts the value from `username`.
    """
    if user.username:
        validator = EmailValidator('Username has to be a valid email')
        validator(user.username)
        # if user.email and user.username != user.email:
        # raise ValidationError('Email must be the same as username.')
        user.email = user.username

User.clean = _user_clean


# Oplossing om e-mail als username te gebruiken
@receiver(pre_save, sender=User)
def enforce_user_clean(sender, instance=None, **kwargs):
    """
    Make sure our validation logic is invoked every time a user gets saved.
    (The default is to only validate when a model form is used.)
    """
    instance.clean()


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Land, LandAdmin)
admin.site.register(Adres, AdresAdmin)
admin.site.register(Woonplaats)
