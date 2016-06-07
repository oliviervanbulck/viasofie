from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from .models import FaqItem, Partner


class FaqItemAdmin(admin.ModelAdmin):
    actions = ('set_active', 'set_inactive',)
    list_display = ('titel', 'actief',)

    def set_active(self, request, queryset):
        queryset.update(actief=True)

    def set_inactive(self, request, queryset):
        queryset.update(actief=False)

    set_active.short_description = 'Maak FAQ items actief'
    set_inactive.short_description = 'Maak FAQ items inactief'


class PartnerAdmin(admin.ModelAdmin):
    actions = ('set_active', 'set_inactive',)
    list_display = ('naam', 'klein_logo', 'actief',)
    fields = ('actief', 'naam', 'link', 'klein_logo', 'logo',)
    readonly_fields = ('klein_logo',)
    #exclude = ('logo',)

    def set_active(self, request, queryset):
        queryset.update(actief=True)

    def set_inactive(self, request, queryset):
        queryset.update(actief=False)

    def klein_logo(self, obj):
        return '<img src="%s" style="max-height: 50px;">' % obj.logo.url

    set_active.short_description = 'Maak partners actief'
    set_inactive.short_description = 'Maak partners inactief'

    klein_logo.short_description = 'Logo'
    klein_logo.allow_tags = True



admin.autodiscover()  # Zonder autodiscover vindt Django het geregistreerde model niet!
admin.site.unregister(Site)  # Dit model moet niet in het admin panel verschijnen
admin.site.unregister(Group)

admin.site.register(FaqItem, FaqItemAdmin)
admin.site.register(Partner, PartnerAdmin)
