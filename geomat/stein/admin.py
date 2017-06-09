from django.contrib import admin

from geomat.stein.models import Classification, CrystalSystem, Handpiece, MineralType, Photograph


class PhotographInline(admin.TabularInline):
    model = Photograph


class ClassificationInline(admin.TabularInline):
    model = Classification


class CrystalSystemInline(admin.TabularInline):
    model = CrystalSystem


class HandpieceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'list_mineral_types', 'finding_place',
                    'current_location', 'last_modified', )
    inlines = [
        PhotographInline,
    ]


admin.site.register(Handpiece, HandpieceAdmin)


class CrystallSystemAdmin(admin.ModelAdmin):
    list_display = ('pk', )


admin.site.register(CrystalSystem, CrystallSystemAdmin)


class MineralTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'trivial_name', 'created_at', 'last_modified', )

    inlines = [
        ClassificationInline,
        CrystalSystemInline,
    ]


admin.site.register(MineralType, MineralTypeAdmin)


class PhotographAdmin(admin.ModelAdmin):
    list_display = ('pk', 'handpiece', )


admin.site.register(Photograph, PhotographAdmin)
