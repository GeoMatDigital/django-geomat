"""URL definitions for REST framework"""
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from geomat.feedback.views import FeedBackView


from geomat.stein.views import (
    CrystalsystemEndpoint,
    FilterCrystalSystemList,
    FilterHandpieceList,
    FilterMineraltypeList,
    FilterPhotographList,
    HandpieceEndpoint,
    MineraltypeEndpoint,
    PhotographEndpoint,
    QuizQuestionEndpoint,
    QuizAnswerEndpoint,
    MineraltypeProfiles,
    GlossaryView
)

app_name = "api"
# Detail and List views via Routers
router = SimpleRouter()
router.register(r'crystalsystem', CrystalsystemEndpoint)
router.register(r'handpiece', HandpieceEndpoint)
router.register(r'photograph', PhotographEndpoint)
router.register(r'mineraltype', MineraltypeEndpoint)
router.register(r'quizquestion', QuizQuestionEndpoint)
router.register(r'quizanswer', QuizAnswerEndpoint)

urlpatterns = [
    # Api Documentation

    url(r'^', include('docs.api_docs', namespace='api_docs')),

    # Feedback
    url(r'^feedback',
        FeedBackView.as_view(),
        name='feedback'),

  
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
    # Mineral Profiles View
    url(
        r'^profiles',
        MineraltypeProfiles.as_view(),
        name=MineraltypeProfiles.name
    ),
    # Glossary View
    url(
        r'^glossary',
        GlossaryView.as_view(),
        name=GlossaryView.name
    ),
]

urlpatterns += router.urls

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'yaml'])
