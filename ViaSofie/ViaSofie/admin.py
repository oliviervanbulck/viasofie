from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django import forms
from .models import FaqItem, Partner


class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.initial['tekst'] = self.test_funct()

    def test_funct(self):
        return 'maybe this twerks?'


class FaqItemAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FaqItemAdminForm, self).__init__(*args, **kwargs)
        self.initial['tekst'] = self.vervang_br_door_newline(self.instance.tekst)

    def vervang_br_door_newline(self, tekst):
        return tekst.replace('<br>', '\r\n')


class FaqItemAdmin(admin.ModelAdmin):
    form = FaqItemAdminForm
    #fields = ('actief', 'titel', 'tekst_met_newline',)

admin.autodiscover()  # Zonder autodiscover vindt Django het geregistreerde model niet!
admin.site.unregister(Site)  # Dit model moet niet in het admin panel verschijnen
admin.site.unregister(Group)

admin.site.register(FaqItem, FaqItemAdmin)
admin.site.register(Partner)
