from django.contrib import admin

# Register your models here.
from django.contrib.admin import SimpleListFilter

from panden.models import Pand, Type, Kenmerk, PandImmoLink, Foto, PandKenmerkPerPand, CarouselFoto


class PandFotoFilter(admin.SimpleListFilter):
    title = 'Pand'
    parameter_name = 'pand'

    def lookups(self, request, model_admin):
        panden = Pand.objects.filter(dossier__actief=True)
        return [(p.id, p.__str__) for p in panden]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(pand__id__exact=self.value())
        else:
            return queryset


class FotoAdmin(admin.ModelAdmin):
    list_display = ('pand_foto',)
    list_per_page = 10
    readonly_fields = ('pand_foto',)
    list_filter = (PandFotoFilter,)

    def pand_foto(self, obj):
        return '<img src="%s" style="max-width: 150px;max-height:150px;" />' % obj.foto.url

    pand_foto.allow_tags = True


class CarouselFotoAdmin(admin.ModelAdmin):
    list_display = ('carousel_foto','actief')
    list_per_page = 10
    readonly_fields = ('carousel_foto',)

    def carousel_foto(self, obj):
        return '<img src="%s" style="max-width: 150px;max-height:150px;" />' % obj.foto.url

    carousel_foto.allow_tags = True


class PandAdmin(admin.ModelAdmin):
    readonly_fields = ('fotos',)

    def fotos(self, obj):
        html = ""
        for obj in Foto.objects.filter(pand_id__exact=obj.id):
            html += '<a href="%s"><img src="%s" style="max-width: 150px;max-height:150px;margin-right:10px;" /></a>'\
                    % (obj.get_admin_url(), obj.foto.url)
        html += '<br /><br /><p><a href="/admin/panden/foto/add/?pand=%s">+ Foto toevoegen</a></p>' % obj.pand_id
        return html

    fotos.allow_tags = True


admin.site.register(Pand, PandAdmin)
admin.site.register(Type)
admin.site.register(Kenmerk)
admin.site.register(PandImmoLink)
admin.site.register(Foto, FotoAdmin)
admin.site.register(CarouselFoto, CarouselFotoAdmin)
admin.site.register(PandKenmerkPerPand)
