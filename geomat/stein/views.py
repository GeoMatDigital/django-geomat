from django.views.generic.list import ListView
from django.shortcuts import render
from .models import CrystalSystem, Handpiece, MineralType, Photograph
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a05fe75... Created basic GET views, tests not working jet
from .serializers import CrystalSystemSerializer, HandpieceSerializer, MineralTypeSerializer, PhotographSerializer
from rest_framework.decorators import api_view

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

<<<<<<< HEAD
=======
>>>>>>> 90d581e... Created apiurls in the right directory and edited the right urls,
=======
>>>>>>> a05fe75... Created basic GET views, tests not working jet

class GalleryListView(ListView):
    model = Photograph
    template_name = 'pages/preview.html'

@api
def gallery_view(request):
    sorting_dict = {
        "list1": [34, 29, 31, 32, 35, 144, 99, 38, 43, 44, 40, 39, 98, 46, 41, 42,
    36, 139, 37, 47, 48, 151, 152, 153, 131, 97, 132, 133, 134, 135,
    113, 126, 117, 118, 122, 140, 74, 127, 49, 46, 50, 54, 55, 52,
    53, 51, 150, 58, 56, 154, 59, 60, 61, 62, 63, 64, 67, 148, 65,
    66, 68, 76, 77, 78, 79, 80, 75, 69, 70, 71, 143, 123, 72, 73,
    124, 103, 102, 83, 82, 147, 81, 125, 84, 85, 145, 137, 136,
    142, 141, 100, 101, 112, 104, 138, 108, 110, 111, 114, 115, 149,
    106, 107, 119, 120, 116, 130, 129, 109, 105, 128],

    }
    sorted_photo_list_dict = {

    }
    for name, id_list in sorting_dict.items():
        all_photos = list(Photograph.objects.filter(pk__in=id_list))
        all_photos.sort(key=lambda x: id_list.index(x.pk))
        sorted_photo_list_dict["{}".format(name)] = all_photos

    return render(request, "pages/preview.html", {"photograph_dict": sorted_photo_list_dict})

# API Views


def handpiece_detail(request, pk):

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a05fe75... Created basic GET views, tests not working jet
    try:
        handpiece = Handpiece.objects.get(pk=pk)
    except Handpiece.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HandpieceSerializer(handpiece)
        return JsonResponse(serializer.data)
<<<<<<< HEAD
=======
    pass
>>>>>>> 90d581e... Created apiurls in the right directory and edited the right urls,
=======
>>>>>>> a05fe75... Created basic GET views, tests not working jet


def crystalsystem_detail(request, pk):

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a05fe75... Created basic GET views, tests not working jet
    try:
        crystalsystem = CrystalSystem.objects.get(pk=pk)
    except CrystalSystem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CrystalSystemSerializer(crystalsystem)
        return JsonResponse(serializer.data)
<<<<<<< HEAD


def photograph_detail(request, pk):

    try:
        photograph = Photograph.objects.get(pk=pk)
    except Photograph.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PhotographSerializer(photograph)
        return JsonResponse(serializer.data)


def mineraltype_detail(request, pk):

    try:
        mineraltype = MineralType.objects.get(pk=pk)
    except MineralType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MineralTypeSerializer(mineraltype)
        return JsonResponse(serializer.data)
=======
    pass
=======
>>>>>>> a05fe75... Created basic GET views, tests not working jet


def photograph_detail(request, pk):

    try:
        photograph = Photograph.objects.get(pk=pk)
    except Photograph.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PhotographSerializer(photograph)
        return JsonResponse(serializer.data)


def mineraltype_detail(request, pk):

    try:
        mineraltype = MineralType.objects.get(pk=pk)
    except MineralType.DoesNotExist:
        return HttpResponse(status=404)

<<<<<<< HEAD
    pass
>>>>>>> 90d581e... Created apiurls in the right directory and edited the right urls,
=======
    if request.method == 'GET':
        serializer = MineralTypeSerializer(mineraltype)
        return JsonResponse(serializer.data)
>>>>>>> a05fe75... Created basic GET views, tests not working jet

