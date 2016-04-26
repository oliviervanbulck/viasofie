from django.contrib import admin

# Register your models here.
from panden.models import Pand, Type, Kenmerk, PandImmoLink, Foto, PandKenmerkPerPand


class FotoAdmin(admin.ModelAdmin):
    list_display = ('pand_foto',)
    list_per_page = 10

    def pand_foto(self, obj):
        return '<img src="%s" style="max-width: 150px;max-height:150px;" />' % obj.foto.url

    pand_foto.allow_tags = True


admin.site.register(Pand)
admin.site.register(Type)
admin.site.register(Kenmerk)
admin.site.register(PandImmoLink)
admin.site.register(Foto, FotoAdmin)
admin.site.register(PandKenmerkPerPand)
