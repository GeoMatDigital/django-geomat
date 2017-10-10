from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import Textarea
from django.contrib.postgres.fields import ArrayField

from geomat.stein.models import Classification, CrystalSystem, Handpiece, MineralType, Photograph, GlossaryEntry


class PhotographInline(admin.TabularInline):
    model = Photograph


class CrystalSystemInline(admin.TabularInline):
    model = CrystalSystem


class HandpieceAdmin(admin.ModelAdmin):
    list_display = ('name', 'link_mineral_types', 'created_at',
                    'last_modified', 'id')

    inlines = [
        PhotographInline,
    ]

    def link_mineral_types(self, obj):
        """
        Retrieve all `MineralType` objects, grabs their ID and creates a
        link to show in the columns.
        """
        l = []
        mineral_types = obj.mineral_type.all()
        for mt in mineral_types:
            url = reverse("admin:stein_mineraltype_change", args=[mt.pk])

            l.append('<a href="{}">{}</a>'.format(url, mt.trivial_name))
        return ', '.join(l)

    link_mineral_types.allow_tags = True
    link_mineral_types.short_description = _('mineral type(s)')


admin.site.register(Handpiece, HandpieceAdmin)


class CrystallSystemAdmin(admin.ModelAdmin):
    list_display = ('mineral_type', 'crystal_system', 'temperature',
                    'pressure')


admin.site.register(CrystalSystem, CrystallSystemAdmin)


class MineralTypeAdmin(admin.ModelAdmin):
    list_display = ('trivial_name', 'classification', 'systematics', 'variety',
                    'minerals', 'mohs_scale', 'created_at', 'last_modified',
                    'id')

    inlines = [
        CrystalSystemInline,
    ]


admin.site.register(MineralType, MineralTypeAdmin)


class PhotographAdmin(admin.ModelAdmin):
    list_display = ('handpiece', 'orientation', 'shot_type', 'created_at',
                    'last_modified', 'id')


admin.site.register(Photograph, PhotographAdmin)


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('classification_name', 'id')


admin.site.register(Classification, ClassificationAdmin)


class GlossaryEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'description')
    formfield_overrides = {
        ArrayField: {'widget': Textarea},
    }


admin.site.register(GlossaryEntry, GlossaryEntryAdmin)
