# -*- coding: utf-8 -*-
"""Views file for stein app"""
import ast

from django.db.models import Count, Case, When
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls import reverse
from django.utils.translation import ugettext_lazy
from django.utils import translation
from django.utils.text import format_lazy
from django.utils.translation import pgettext_lazy

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from geomat.stein.models import (
    CrystalSystem,
    GlossaryEntry,
    Handpiece,
    MineralType,
    Photograph,
    QuizAnswer,
    QuizQuestion
)
from geomat.stein.serializers import (
    CrystalSystemFullSerializer,
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
    """
    A View which creates a filters dict and returns a List of objects matching alle given Filters.
    View only for Retrieving Data.

    """
    varchar_fields = ()  # Tupel containing all modelfileds which are varcharfields
    int_fields = ()  # Tupel containing all modelfileds which are integerfields
    range_fields = () # Tuple containing all modelfields which are represented by rangefields
    model_fields = ()  # Tupel containing all modelfileds which are Model relation fields those are also ints

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

                # We make the compromise that we only use float_fileds for ranges wich need to be filtered
                # with __contains
                elif field in self.range_fields:
                    filters["{}__contains".format(field)] = float(self.request.GET.get(field, None))
                elif field in self.model_fields:
                    filters[field] = int(self.request.GET.get(field, None))
                else:
                    filters[field] = self.request.GET.get(
                        field, None)  # get the value of the field from request

        return filters

    def get_queryset(self,filters=None):
        """Method which returns the filtered Queryset."""
        filters =  filters if filters else self.get_filters()
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        obj = queryset.filter(**filters)
        return obj


# API Detail views
# This section is for all ReadOnly Endpoints meaning they only define GET'able Endpoints.
# To achieve this we utilize the ReadOnlyModelViewSet for DRF.


class HandpieceEndpoint(ReadOnlyModelViewSet):
    """
    This Endpoint reflects the Databasetable of all existing Handpieces.
    Therefor it's a GET only Endpoint.
    The routing for the collection and the idividual resource is handled by the Viewset.
    """
    queryset = Handpiece.objects.all()
    serializer_class = HandpieceSerializer
    name = 'handpiece'


class CrystalsystemEndpoint(ReadOnlyModelViewSet):
    """
    This Endpoint reflects the Databasetable of all existing Crystalsystems.
    Therefor it's a GET only Endpoint.
    The routing for the collection and the idividual resource is handled by the Viewset.
    """
    queryset = CrystalSystem.objects.all()
    serializer_class = CrystalSystemFullSerializer
    name = 'crystalsystem'


class MineraltypeEndpoint(ReadOnlyModelViewSet):
    """
    This Endpoint reflects the Databasetable of all existing Handpieces.
    Therefor it's a GET only Endpoint.
    The routing for the collection and the idividual resource is handled by the Viewset.
    """
    queryset = MineralType.objects.all()
    serializer_class = MineralTypeSerializer
    name = 'mineraltype'


class PhotographEndpoint(ReadOnlyModelViewSet):
    """
    This Endpoint reflects the Databasetable of all existing Photographs.
    Therefor it's a GET only Endpoint.
    The routing for the collection and the idividual resource is handled by the Viewset.
    """
    queryset = Photograph.objects.all()
    serializer_class = PhotographSerializer
    name = 'photograph'


class QuizQuestionEndpoint(ReadOnlyModelViewSet):
    """
    This Endpoint reflects the Databasetable of all existing QuizQuestions.
    Therefor it's a GET only Endpoint.
    The routing for the collection and the idividual resource is handled by the Viewset.
    """
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionFullSerializer
    name = 'quizquestion'

class QuizAnswerEndpoint(ReadOnlyModelViewSet):
    """
    This Endpoint reflects the Databasetable of all existing QuizAnswers.
    Therefor it's a GET only Endpoint.
    The routing for the collection and the idividual resource is handled by the Viewset.
    """
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerFullSerializer
    name = 'quizanswer'


# Filter API Views
# This is an Invention to retrieve resources or collections filtered according to the
# Database fields and their values.
# This Endpoints are also ReadOnly Endpoints and hence only GET'able


class FilterMineraltypeList(ListFilterAPIView):
    """
    This is a Filter Endpoint. It allows to filter it's Resource according to the
    databasefields an their values.
    Providing a field and it's value to filter by just use the common GET syntax.
    This Means :
    * url\?\<first_fieldname\>\=value1\&\<second_fieldname\>\=value2

    Resource :
    * MineralType

    Fields available for this Resource are :
    &nbsp;&nbsp;&nbsp;&nbsp;trivial_name, systematics, variety, minerals,
    &nbsp;&nbsp;&nbsp;&nbsp;mohs_scale, density, streak, normal_color,
    &nbsp;&nbsp;&nbsp;&nbsp;fracture, cleavage, lustre, chemical_formula,
    &nbsp;&nbsp;&nbsp;&nbsp;other, resource_mindat, resource_mineralienatlas

    Note to filter for systematics one needs this 'translations' :
    * EL = Elements
    * SF = Sulfides & Sulfosalts
    * HG = Halogenides
    * OH = Oxides and Hydroxides
    * CN = Carbonates and Nitrates
    * BR = Borates
    * SL = Sulfates
    * PV = Phosphates, Arsenates & Vanadates
    * SG = Silicates & Germanates
    * OC = Organic Compounds

    """

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
    range_fields = ('density', 'mohs_scale')


class FilterCrystalSystemList(ListFilterAPIView):
    """
    This is a Filter Endpoint. It allows to filter it's Resource according to the
    databasefields an their values.
    Providing a field and it's value to filter by just use the common GET syntax.

    This Means :
    * url\?\<first_fieldname\>\=value1\&\<second_fieldname\>\=value2

    Resource :
    * Crystalsystem

    Fields available for this Resource are :
    &nbsp;&nbsp;&nbsp;&nbsp;mineral_type, crystal_system, temperature,
    &nbsp;&nbsp;&nbsp;&nbsp;pressure <br>

    Note to filter for mineral_type :
    The value of those fields is the id of a MineralType Resource.

    """

    queryset = CrystalSystem.objects.all()
    serializer_class = CrystalSystemFullSerializer
    name = 'crystalsystem-filter'
    lookup_field = ('mineral_type', 'crystal_system', 'temperature',
                    'pressure')
    int_fields = ('temperature', 'pressure')
    model_fields = ('mineral_type', )


class FilterHandpieceList(ListFilterAPIView):
    """
    This is a Filter Endpoint. It allows to filter it's Resource according to the
    databasefields an their values.
    Providing a field and it's value to filter by just use the common GET syntax.

    This Means :
    * url\?\<first_fieldname\>\=value1\&\<second_fieldname\>\=value2

    Resource :
    * Handpiece

    Fields available for this Resource are:
    &nbsp;&nbsp;&nbsp;&nbsp;name, mineral_type, finding_place,
    &nbsp;&nbsp;&nbsp;&nbsp;current_location, old_inventory_number <br>
    Note to filter for mineral_type:
    The value of those fields is the id of a MineralType Resource.

    """
    queryset = Handpiece.objects.all()
    serializer_class = HandpieceSerializer
    name = 'handpiece-filter'
    lookup_field = ('name', 'mineral_type', 'finding_place',
                    'current_location', 'old_inventory_number')
    model_fields = ('mineral_type', )


class FilterPhotographList(ListFilterAPIView):
    """
    This is a Filter Endpoint. It allows to filter it's Resource according to the
    databasefields an their values.
    Providing a field and it's value to filter by just use the common GET syntax.

    This Means :
    * url\?\<first_fieldname\>\=value1\&\<second_fieldname\>\=value2

    Resource :
    * Handpiece

    Fields available for this Resource are:
    &nbsp;&nbsp;&nbsp;&nbsp;image_file, handpiece, orientation, shot_type,
    &nbsp;&nbsp;&nbsp;&nbsp;online_status, created_at, last_modified <br>
    Note to filter for handpiece:
    The value of those fields is the id of a Handpiece Resource.

    """
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



class GalleryView(generics.ListAPIView):
    queryset = Photograph.objects.all()
    serializer_class = PhotographSerializer
    name = 'gallery'

    def get_queryset(self):
        queryset = super().get_queryset()
        #  do our sorting here
        pk_list= (34, 29, 31, 32, 35, 144, 99, 38, 44, 40, 39, 98, 46, 41, 42, 36, 139,
         37, 47, 48, 151, 152, 153, 131, 97, 132, 133, 134, 135, 113, 126, 117,
         118, 122, 140, 74, 127, 49, 46, 50, 54, 55, 52, 53, 51, 150, 58, 56,
         154, 59, 60, 61, 62, 63, 64, 67, 148, 65, 66, 68, 76, 77, 78, 79, 80,
         75, 69, 70, 71, 143, 123, 72, 73, 124, 100, 101, 137, 136, 142, 141,
         103, 102, 83, 82, 147, 81, 125, 84, 85, 145, 112, 104, 138, 108, 110,
         111, 114, 115, 149, 106, 107, 119, 120, 116, 130, 129, 109, 105, 128)

        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pk_list)])
        queryset = queryset.filter(pk__in=pk_list).order_by(preserved)

        return queryset


# FUTURE API View for the Mineraltype Profiles
# processes a url looking like this :
# profiles/<int:layer>/<str:item>

class FutureMineraltypeProfiles(generics.RetrieveAPIView):
    model = MineralType
    queryset = model.objects.all()
    serializer_class = MineralProfilesSerializer
    name = 'mineraltype-profiles'
    app = "api"
    # layers = {0:MineralType.MINERAL_CATEGORIES,
    #           1:MineralType.SPLIT_CHOICES,
    #           2:MineralType.SUB_CHOICES}

    fields = {0:"systematics",
              1:"split_systematics",
              2:"sub_systematics"}

    def get(self, request, layer, item=None, *args, **kwargs):

        if len(self.fields) == layer:

            field = self.get_layer_field(layer - 1)
            tpl = self.get_choices(field)

            translation.activate('en')
            query = self.get_queryset().filter(**{field: self.get_search_abrev(tpl, item)})
            translation.deactivate()

            return Response(self.get_serializer(query, many=True).data)

        elif len(self.fields) - 1 < layer:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            data = {}
            field = self.get_layer_field(layer)
            tpl = self.get_choices(field)

            for short, entry in tpl:
                key = str(entry)

                translation.activate('en')
                if layer > 0 and not (str(entry) in str(item) or str(item) in str(entry)):
                    translation.deactivate()
                    continue


                translation.activate('en')      # this is a hack
                krgs = {
                    "layer": layer+1,
                    "item": entry}

                data[key] = {"link": reverse("{0}:{1}".format(self.app,self.name),
                                             kwargs=krgs)}
                translation.deactivate()

            if data:
                return Response(data)

            field = self.get_layer_field(layer-1)
            tpl = self.get_choices(field)

            translation.activate('en')
            query = self.get_queryset().filter(**{field:self.get_search_abrev(tpl, item)})
            translation.deactivate()

            return Response(self.get_serializer(query, many=True).data)


    def get_choices(self, field):
        tpl = self.model._meta.get_field(field).choices
        return tpl

    def get_layer_field(self, layer):
        return self.fields[layer]

    def get_search_abrev(self, choices, item):
        return dict((reversed(x) for x in choices))[item]


# Api View for the Glossary
class GlossaryView(generics.ListAPIView):
    queryset = GlossaryEntry.objects.all()
    serializer_class = GlossaryEntrySerializer
    name = 'glossary'
