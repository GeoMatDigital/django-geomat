from django.contrib import admin
from geomat.stein.models import Handpiece, MineralType, Photograph


class PhotographInline(admin.TabularInline):
    model = Photograph

class HandpieceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'list_mineral_types', 'finding_place',
                    'current_location', 'last_modified',)
    inlines = [
        PhotographInline,
    ]

admin.site.register(Handpiece, HandpieceAdmin)


class MineralTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'trivial_name', 'created_at', 'last_modified',)

admin.site.register(MineralType, MineralTypeAdmin)


class PhotographAdmin(admin.ModelAdmin):
    list_display = ('pk', 'handpiece',)

admin.site.register(Photograph, PhotographAdmin)
