"""URL definitions for REST framework"""
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from geomat.stein.views import crystalsystem_detail, handpiece_detail, photograph_detail, \
                               mineraltype_detail, ApiRoot

app_name = "api"
urlpatterns = [
    # Detail Views for Crystalsystems, handpieces, Photographs and Mineraltypes
    url(
        r'^crystalsystem/(?P<pk>[0-9]+)/',
        crystalsystem_detail,
        name="crystalsystem"),
    url(r'^handpiece/(?P<pk>[0-9]+)/', handpiece_detail, name="handpiece"),
    url(r'^photograph/(?P<pk>[0-9]+)/', photograph_detail, name="photograph"),
    url(
        r'^mineraltype/(?P<pk>[0-9]+)/',
        mineraltype_detail,
        name="mineraltype"),
    url(r'^$', ApiRoot.as_view(), name=ApiRoot.name),
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
