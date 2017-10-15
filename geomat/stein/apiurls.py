"""URL definitions for REST framework"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from geomat.stein.views import (
    ClassificationDetail,
    ClassificationList,
    CrystalsystemDetail,
    CrystalsystemList,
    FilterCrystalSystemList,
    FilterHandpieceList,
    FilterMineraltypeList,
    FilterPhotographList,
    HandpieceDetail,
    HandpieceList,
    MineraltypeDetail,
    MineraltypeList,
    PhotographDetail,
    PhotographList,
    ProfileMineraltypeview,
    QuizQuestionList,
    QuizAnswerList,
)

app_name = "api"
urlpatterns = [
    # Detail Views for Crystalsystems, Handpieces, Photographs, Mineraltypes and Classifications
    url(
        r'^crystalsystem/(?P<pk>[0-9]+)/',
        CrystalsystemDetail.as_view(),
        name=CrystalsystemDetail.name),
    url(
        r'^handpiece/(?P<pk>[0-9]+)/',
        HandpieceDetail.as_view(),
        name=HandpieceDetail.name),
    url(
        r'^photograph/(?P<pk>[0-9]+)/',
        PhotographDetail.as_view(),
        name=PhotographDetail.name),
    url(
        r'^mineraltype/(?P<pk>[0-9]+)/',
        MineraltypeDetail.as_view(),
        name=MineraltypeDetail.name),
    url(
        r'^classification/(?P<pk>[0-9]+)',
        ClassificationDetail.as_view(),
        name=ClassificationDetail.name
    ),

    # List Views for Crystalsystems, Handpieces, Photographs and Mineraltypes
    url(
        r'^crystalsystem_list',
        CrystalsystemList.as_view(),
        name=CrystalsystemList.name),
    url(r'^handpiece_list', HandpieceList.as_view(), name=HandpieceList.name),
    url(
        r'^photograph_list',
        PhotographList.as_view(),
        name=PhotographList.name),
    url(
        r'^mineraltype_list',
        MineraltypeList.as_view(),
        name=MineraltypeList.name),
    url(r'^classification_list',
        ClassificationList.as_view(),
        name=ClassificationList.name),

    # Filter Views for Crystalsystems, Handpieces, Photographs and Mineraltypes
    url(
        r'^mineraltype_filter',
        FilterMineraltypeList.as_view(),
        name=FilterMineraltypeList.name),
    url(
        r'^crystalsystem_filter',
        FilterCrystalSystemList.as_view(),
        name=FilterCrystalSystemList.name),
    url(
        r'^handpiece_filter',
        FilterHandpieceList.as_view(),
        name=FilterHandpieceList.name),
    url(
        r'^photograph_filter',
        FilterPhotographList.as_view(),
        name=FilterPhotographList.name),
    url(
        r'^mineral_profiles',
        ProfileMineraltypeview.as_view(),
        name=ProfileMineraltypeview.name
    ),
    url(r"^quizquestion_list",
        QuizQuestionList.as_view(),
        name=QuizQuestionList.name),
    url(r"^quizanswer_list",
        QuizAnswerList.as_view(),
        name=QuizAnswerList.name)
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
