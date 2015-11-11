from django.contrib import admin
from geomat.stein.models import Handpiece


class HandpieceAdmin(admin.ModelAdmin):
    list_display = ('pk', '__unicode__', 'mineral_type', 'finding_place',
                    'current_location', 'last_modified',)

admin.site.register(Handpiece, HandpieceAdmin)
