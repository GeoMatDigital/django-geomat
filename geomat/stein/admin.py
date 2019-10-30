from django.contrib import admin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html, format_html_join
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from mutagen.mp3 import MP3

from geomat.stein.models import (
    Cleavage,
    CrystalSystem,
    GlossaryEntry,
    Handpiece,
    MineralType,
    Photograph,
    QuizAnswer,
    QuizQuestion,
    TreeNode
)
from geomat.stein.admin_forms import QuizQuestionAdminForm, QuizAnswerAdminForm


class CleavageInline(admin.TabularInline):
    model = Cleavage


class PhotographInline(admin.TabularInline):
    model = Photograph


class CrystalSystemInline(admin.TabularInline):
    model = CrystalSystem


class CleavageAdmin(admin.ModelAdmin):
    list_display = ("cleavage", "coordinates", "mineral_type")


admin.site.register(Cleavage, CleavageAdmin)


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

            l.append((url, mt.trivial_name))
        return format_html_join(', ', '<a href="{}">{}</a>', l)

    link_mineral_types.allow_tags = True
    link_mineral_types.short_description = _('mineral type(s)')


admin.site.register(Handpiece, HandpieceAdmin)


class CrystallSystemAdmin(admin.ModelAdmin):
    list_display = ('mineral_type', 'crystal_system', 'temperature',
                    'pressure')


admin.site.register(CrystalSystem, CrystallSystemAdmin)


class MineralTypeAdmin(admin.ModelAdmin):
    list_display = ('trivial_name', 'variety',
                    'minerals', 'created_at', 'last_modified',
                    'id')

    inlines = [CrystalSystemInline, CleavageInline]


admin.site.register(MineralType, MineralTypeAdmin)


class PhotographAdmin(admin.ModelAdmin):
    list_display = ('handpiece',  'created_at', 'last_modified', 'id')
    readonly_fields = ('audio_duration',)

    def save_model(self, request, obj, form, change):
        super(PhotographAdmin, self).save_model(request, obj, form, change)
        if obj.audio_file:
            obj.audio_duration = MP3(obj.audio_file).info.length
            obj.save()


admin.site.register(Photograph, PhotographAdmin)


class GlossaryEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'description')


admin.site.register(GlossaryEntry, GlossaryEntryAdmin)


class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_question', 'correct', 'atext')
    form = QuizAnswerAdminForm

    def link_question(self, obj):
        """
        Retrieve all `MineralType` objects, grabs their ID and creates a
        link to show in the columns.
        """
        element = ""
        question = obj.question

        url = reverse("admin:stein_mineraltype_change", args=[question.pk])

        return format_html('<a href="{}">{}</a>', url, question.pk)

    link_question.allow_tags = True
    link_question.short_description = _('question')


class QuizAnswerInline(admin.TabularInline):
    model = QuizAnswer


admin.site.register(QuizAnswer, QuizAnswerAdmin)


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tags', 'difficulty', 'qtype')
    inlines = [QuizAnswerInline]
    form = QuizQuestionAdminForm


admin.site.register(QuizQuestion, QuizQuestionAdmin)


admin.site.register(TreeNode, MPTTModelAdmin)
