from django.contrib import admin
from geomat.stein.models import Handpiece, MineralType, Photograph


class HandpieceAdmin(admin.ModelAdmin):
    list_display = ('pk', '__unicode__', 'list_mineral_types', 'finding_place',
                    'current_location', 'last_modified',)

admin.site.register(Handpiece, HandpieceAdmin)


class MineralTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', '__unicode__', 'created_at', 'last_modified',)

admin.site.register(MineralType, MineralTypeAdmin)

admin.site.register(Photograph)
