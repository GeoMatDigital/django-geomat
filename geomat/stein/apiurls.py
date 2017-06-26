"""URL definitions for REST framework"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from geomat.stein.views import CrystalsystemDetail, HandpieceDetail, PhotographDetail, MineraltypeDetail, \
    CrystalsystemList, HandpieceList, PhotographList, MineraltypeList, FilterMineraltypeList, \
    FilterCrystalSystemList, FilterHandpieceList, FilterPhotographList

app_name = "api"
urlpatterns = [
    # Detail Views for Crystalsystems, Handpieces, Photographs and Mineraltypes
    url(
        r'^crystalsystem/(?P<pk>[0-9]+)/',
        CrystalsystemDetail.as_view(),
        name="crystalsystem"),
    url(r'^handpiece/(?P<pk>[0-9]+)/', HandpieceDetail.as_view(), name="handpiece"),
    url(r'^photograph/(?P<pk>[0-9]+)/', PhotographDetail.as_view(), name="photograph"),
    url(
        r'^mineraltype/(?P<pk>[0-9]+)/',
        MineraltypeDetail.as_view(),
        name="mineraltype"),

    # List Views for Crystalsystems, Handpieces, Photographs and Mineraltypes

    url(r'^crystalsystem_list', CrystalsystemList.as_view(), name=CrystalsystemList.name),
    url(r'handpiece_list', HandpieceList.as_view(), name=HandpieceList.name),
    url(r'photograph_list', PhotographList.as_view(), name=PhotographList.name),
    url(r'mineraltype_list', MineraltypeList.as_view(), name=MineraltypeList.name),

    # Filter Views for Crystalsystems, Handpieces, Photographs and Mineraltypes

    url(r'mineraltype_filter', FilterMineraltypeList.as_view(), name=FilterMineraltypeList.name),
    url(r'crystalsystem_filter', FilterCrystalSystemList.as_view(), name=FilterCrystalSystemList.name),
    url(r'handpiece_filter', FilterHandpieceList.as_view(), name=FilterHandpieceList.name),
    url(r'photograph_filter', FilterPhotographList.as_view(), name=FilterPhotographList.name)
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
