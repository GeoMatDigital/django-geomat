# -*- coding: utf-8 -*-
"""Views file for stein app"""
import ast

from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework import generics
from rest_framework.response import Response

from geomat.stein.models import (
    Classification,
    CrystalSystem,
    GlossaryEntry,
    Handpiece,
    MineralType,
    Photograph,
    QuizAnswer,
    QuizQuestion
)
from geomat.stein.serializers import (
    ClassificationSerializer,
    CrystalSystemSerializer,
    GlossaryEntrySerializer,
    HandpieceSerializer,
    MineralProfilesSerializer,
    MineralTypeSerializer,
    PhotographSerializer,
    QuizAnswerFullSerializer,
    QuizQuestionFullSerializer
)


class GalleryListView(ListView):
    model = Photograph
    template_name = 'pages/preview.html'


def gallery_view(request):
    sorting_dict = {
        "list1":
        (34, 29, 31, 32, 35, 144, 99, 38, 44, 40, 39, 98, 46, 41, 42, 36, 139,
         37, 47, 48, 151, 152, 153, 131, 97, 132, 133, 134, 135, 113, 126, 117,
         118, 122, 140, 74, 127, 49, 46, 50, 54, 55, 52, 53, 51, 150, 58, 56,
         154, 59, 60, 61, 62, 63, 64, 67, 148, 65, 66, 68, 76, 77, 78, 79, 80,
         75, 69, 70, 71, 143, 123, 72, 73, 124, 100, 101, 137, 136, 142, 141,
         103, 102, 83, 82, 147, 81, 125, 84, 85, 145, 112, 104, 138, 108, 110,
         111, 114, 115, 149, 106, 107, 119, 120, 116, 130, 129, 109, 105, 128),
    }
    sorted_photo_list_dict = {}
    for name, id_list in list(sorting_dict.items()):
        all_photos = list(Photograph.objects.filter(pk__in=id_list))
        all_photos.sort(key=lambda x: id_list.index(x.pk))
        sorted_photo_list_dict["{}".format(name)] = all_photos

    return render(request, "preview.html",
                  {"photograph_dict": sorted_photo_list_dict})


# API Views
# Custom Views


class ListFilterAPIView(generics.ListAPIView):
    """ A View which creates a filters dict and returns a List of objects matching alle given Filters.
        View only for Retrieving Data."""
    varchar_fields = (
    )  # Tupel containing all modelfileds which are varcharfields
    int_fields = ()  # Tupel containing all modelfileds which are integerfields
    model_fields = (
    )  # Tupel containing all modelfileds which are Model relation fields those are also ints

    def get_filters(self):
        """ Method which creates the filters dict.
        Matches the given Parameters from the request with the allowed lookup_fields, and only maps non-empty fields.
        """
        filters = {}
        for field in self.lookup_field:  # goes on for every field we defined as lookup_field
            if self.request.GET.get(field, None):
                if field in self.varchar_fields:  # we do not want the filter to contain "empty" fields
                    filters[field] = ast.literal_eval(
                        self.request.GET.get(field, None))
                elif field in self.int_fields:  # Modelreferences are searched by pk
                    filters[field] = int(self.request.GET.get(field, None))
                elif field in self.model_fields:
                    filters[field] = int(self.request.GET.get(field, None))
                else:
                    filters[field] = self.request.GET.get(
                        field, None)  # get the value of the field from request

        return filters

    def get_queryset(self):
        """Method which returns the filtered Queryset."""
        filters = self.get_filters()
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        obj = queryset.filter(**filters)
        return obj


# API Detail views


class HandpieceDetail(generics.RetrieveAPIView):
    queryset = Handpiece.objects.all()
    serializer_class = HandpieceSerializer
    name = 'handpiece'


class CrystalsystemDetail(generics.RetrieveAPIView):
    queryset = CrystalSystem.objects.all()
    serializer_class = CrystalSystemSerializer
    name = 'crystalsystem'


class MineraltypeDetail(generics.RetrieveAPIView):
    queryset = MineralType.objects.all()
    serializer_class = MineralTypeSerializer
    name = 'mineraltype'


class PhotographDetail(generics.RetrieveAPIView):
    queryset = Photograph.objects.all()
    serializer_class = PhotographSerializer
    name = 'photograph'


class ClassificationDetail(generics.RetrieveAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    name = 'classification'


class QuizQuestionDetail(generics.RetrieveAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionFullSerializer
    name = 'quizquestion'


class QuizAnswerDetail(generics.RetrieveAPIView):
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerFullSerializer
    name = 'quizanswer'


# API List views


class HandpieceList(generics.ListAPIView):
    queryset = Handpiece.objects.all()
    serializer_class = HandpieceSerializer
    name = 'handpiece-list'


class CrystalsystemList(generics.ListAPIView):
    """

    This is a test

    """
    queryset = CrystalSystem.objects.all()
    serializer_class = CrystalSystemSerializer
    name = 'crystalsystem-list'

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MineraltypeList(generics.ListAPIView):

    #    queryset = MineralType.objects.annotate(handpiece_count=Count('handpiece')).all()
    queryset = MineralType.objects.all()
    serializer_class = MineralTypeSerializer
    name = 'mineraltype-list'


class PhotographList(generics.ListAPIView):
    queryset = Photograph.objects.all()
    serializer_class = PhotographSerializer
    name = 'photograph-list'


class ClassificationList(generics.ListAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    name = 'classification-list'


class QuizQuestionList(generics.ListAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionFullSerializer
    name = 'quizquestion-list'


class QuizAnswerList(generics.ListAPIView):
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerFullSerializer
    name = 'quizanswer-list'


# Filter API Views


class FilterMineraltypeList(ListFilterAPIView):
    queryset = MineralType.objects.all()
    serializer_class = MineralTypeSerializer
    name = 'mineraltype-filter'
    lookup_field = ('trivial_name', 'systematics', 'variety', 'minerals',
                    'mohs_scale', 'density', 'streak', 'normal_color',
                    'fracture', 'cleavage', 'lustre', 'chemical_formula',
                    'other', 'resource_mindat', 'resource_mineralienatlas')
    varchar_fields = (
        'fracture',
        'cleavage',
        'lustre', )


class FilterCrystalSystemList(ListFilterAPIView):
    queryset = CrystalSystem.objects.all()
    serializer_class = CrystalSystemSerializer
    name = 'crystalsystem-filter'
    lookup_field = ('mineral_type', 'crystal_system', 'temperature',
                    'pressure')
    int_fields = ('temperature', 'pressure')
    model_fields = ('mineral_type', )


class FilterHandpieceList(ListFilterAPIView):
    queryset = Handpiece.objects.all()
    serializer_class = HandpieceSerializer
    name = 'handpiece-filter'
    lookup_field = ('name', 'mineral_type', 'finding_place',
                    'current_location', 'old_inventory_number')
    model_fields = ('mineral_type', )


class FilterPhotographList(ListFilterAPIView):
    queryset = Photograph.objects.all()
    serializer_class = PhotographSerializer
    name = 'photograph-filter'
    lookup_field = ('image_file', 'handpiece', 'orientation', 'shot_type',
                    'online_status', 'created_at', 'last_modified')
    model_fields = ('handpiece', )


# API View for the Mineraltype Profiles
class MineraltypeProfiles(generics.ListAPIView):
    queryset = MineralType.objects.all()
    serializer_class = MineralProfilesSerializer
    name = 'mineraltype-profiles'


# Api View for the Glossary
class GlossaryView(generics.ListAPIView):
    queryset = GlossaryEntry.objects.all()
    serializer_class = GlossaryEntrySerializer
    name = 'glossary'
