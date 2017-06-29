from django.contrib import admin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from geomat.stein.models import Classification, CrystalSystem, Handpiece, MineralType, Photograph


class PhotographInline(admin.TabularInline):
    model = Photograph


# class ClassificationInline(admin.TabularInline):
#     model = Classification


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
    list_display = ('trivial_name', 'systematics', 'variety', 'minerals',
                    'mohs_scale', 'created_at', 'last_modified', 'id')

    inlines = [
        # ClassificationInline,
        CrystalSystemInline,
    ]


admin.site.register(MineralType, MineralTypeAdmin)


class PhotographAdmin(admin.ModelAdmin):
    list_display = ('handpiece', 'orientation', 'shot_type', 'created_at',
                    'last_modified', 'id')


admin.site.register(Photograph, PhotographAdmin)


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'classification_name')


admin.site.register(Classification, ClassificationAdmin)
