"""Views file for stein app"""
import ast

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework import generics

from geomat.stein.models import CrystalSystem, Handpiece, MineralType, Photograph
from geomat.stein.serializers import CrystalSystemSerializer, HandpieceSerializer, \
    MineralTypeSerializer, PhotographSerializer


class GalleryListView(ListView):
    model = Photograph
    template_name = 'pages/preview.html'


def gallery_view(request):
    sorting_dict = {
        "list1": [
            34, 29, 31, 32, 35, 144, 99, 38, 43, 44, 40, 39, 98, 46, 41, 42,
            36, 139, 37, 47, 48, 151, 152, 153, 131, 97, 132, 133, 134, 135,
            113, 126, 117, 118, 122, 140, 74, 127, 49, 46, 50, 54, 55, 52, 53,
            51, 150, 58, 56, 154, 59, 60, 61, 62, 63, 64, 67, 148, 65, 66, 68,
            76, 77, 78, 79, 80, 75, 69, 70, 71, 143, 123, 72, 73, 124, 103,
            102, 83, 82, 147, 81, 125, 84, 85, 145, 137, 136, 142, 141, 100,
            101, 112, 104, 138, 108, 110, 111, 114, 115, 149, 106, 107, 119,
            120, 116, 130, 129, 109, 105, 128
        ],
    }
    sorted_photo_list_dict = {}
    for name, id_list in sorting_dict.items():
        all_photos = list(Photograph.objects.filter(pk__in=id_list))
        all_photos.sort(key=lambda x: id_list.index(x.pk))
        sorted_photo_list_dict["{}".format(name)] = all_photos

    return render(request, "pages/preview.html",
                  {"photograph_dict": sorted_photo_list_dict})


# API Views
# Custom Views

class ListFilterAPIView(generics.ListAPIView):
    """ A View which creates a filters dict and returns a List of objects matching alle given Filters.
        View only for Retrieving Data."""
    varchar_fields = ()         # Tupel containing all modelfileds which are varcharfields
    int_fields = ()             # Tupel containing all modelfileds which are integerfields
    model_fields = ()           # Tupel containing all modelfileds which are Model relation fields those are also ints

    def get_filters(self):
        """ Method which creates the filters dict.
        Matches the given Parameters from the request with the allowed lookup_fields, and only maps non-empty fields.
        """
        filters = {}
        for field in self.lookup_field:  # goes on for every field we defined as lookup_field
            if self.request.GET.get(field, None):
                if field in self.varchar_fields:  # we do not want the filter to contain "empty" fields
                    filters[field] = ast.literal_eval(self.request.GET.get(field, None))
                elif field in self.int_fields:  # Modelreferences are searched by pk
                    filters[field] = int(self.request.GET.get(field, None))
                elif field in self.model_fields:
                    filters[field] = int(self.request.GET.get(field, None))
                else:
                    filters[field] = self.request.GET.get(field, None)  # get the value of the field from request

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


# API List views


class HandpieceList(generics.ListAPIView):
    queryset = Handpiece.objects.all()
    serializer_class = HandpieceSerializer
    name = 'handpiece-list'


class CrystalsystemList(generics.ListAPIView):
    queryset = CrystalSystem.objects.all()
    serializer_class = CrystalSystemSerializer
    name = 'crystalsystem-list'


class MineraltypeList(generics.ListAPIView):
    queryset = MineralType.objects.all()
    serializer_class = MineralTypeSerializer
    name = 'mineraltype-list'


class PhotographList(generics.ListAPIView):
    queryset = Photograph.objects.all()
    serializer_class = PhotographSerializer
    name = 'photograph-list'


# Filter API Views


class FilterMineraltypeList(ListFilterAPIView):
    queryset = MineralType.objects.all()
    serializer_class = MineralTypeSerializer
    name = 'mineraltype-filter'
    lookup_field = ('trivial_name', 'systematics', 'variety', 'minerals',
                    'mohs_scale', 'density', 'streak', 'normal_color',
                    'fracture', 'cleavage', 'lustre', 'chemical_formula',
                    'other', 'resource_mindat', 'resource_mineralienatlas')
    varchar_fields = ('fracture', 'cleavage', 'lustre',)


class FilterCrystalSystemList(ListFilterAPIView):
    queryset = CrystalSystem.objects.all()
    serializer_class = CrystalSystemSerializer
    name = 'crystalsystem-filter'
    lookup_field = ('mineral_type', 'crystal_system', 'temperature', 'pressure')
    int_fields = ('temperature', 'pressure')
    model_fields = ('mineral_type',)


class FilterHandpieceList(ListFilterAPIView):
    queryset = Handpiece.objects.all()
    serializer_class = HandpieceSerializer
    name = 'handpiece-filter'
    lookup_field = ('name', 'mineral_type', 'finding_place', 'current_location',
                    'old_inventory_number')
    model_fields = ('mineral_type',)

# @api_view(('GET', ))
# @permission_classes((permissions.AllowAny, ))
# @renderer_classes((JSONRenderer, ))
# def handpiece_detail(request, pk, format=None):
#     try:
#         handpiece = Handpiece.objects.get(pk=pk)
#     except Handpiece.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = HandpieceSerializer(handpiece)
#         return JsonResponse(serializer.data, safe=False)


# @api_view(('GET', ))
# @permission_classes((permissions.AllowAny, ))
# @renderer_classes((JSONRenderer, ))
# def crystalsystem_detail(request, pk, format=None):
#     try:
#         crystalsystem = CrystalSystem.objects.get(pk=pk)
#     except CrystalSystem.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = CrystalSystemSerializer(crystalsystem)
#         return JsonResponse(
#             serializer.data,
#             safe=False, )
#
#
# @api_view(('GET', ))
# @permission_classes((permissions.AllowAny, ))
# @renderer_classes((JSONRenderer, ))
# def photograph_detail(request, pk, format=None):
#     try:
#         photograph = Photograph.objects.get(pk=pk)
#     except Photograph.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = PhotographSerializer(photograph)
#         return JsonResponse(serializer.data, safe=False)
#
#
# @api_view(('GET', ))
# @permission_classes((permissions.AllowAny, ))
# @renderer_classes((JSONRenderer, ))
# def mineraltype_detail(request, pk, format=None):
#     try:
#         mineraltype = MineralType.objects.get(pk=pk)
#     except MineralType.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = MineralTypeSerializer(mineraltype)
#         return JsonResponse(serializer.data, safe=False)
