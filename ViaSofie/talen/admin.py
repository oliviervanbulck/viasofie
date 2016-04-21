from django.contrib import admin

# Register your models here.
from talen.models import TaalcodePerLabel, Label, Taalcode

admin.site.register(Label)
admin.site.register(Taalcode)
admin.site.register(TaalcodePerLabel)
