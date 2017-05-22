from django.conf.urls import include, url
<<<<<<< HEAD
<<<<<<< HEAD
from .views import crystalsystem_detail, handpiece_detail, photograph_detail, mineraltype_detail
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"
urlpatterns = [

    # Detail Views for Crystalsystems, handpieces, Photographs and Mineraltypes

    url(r'^crystalsystem/(?P<pk>[0-9]+)/', crystalsystem_detail, name="crystalsystem"),

    url(r'^handpiece/(?P<pk>[0-9]+)/', handpiece_detail, name="handpiece"),

    url(r'photograph/(?P<pk>[0-9]+)/', photograph_detail, name="photograph"),

    url(r'mineraltype/(?P<pk>[0-9]+)/', mineraltype_detail, name="mineraltype"),

]
urlpatterns = format_suffix_patterns(urlpatterns)
=======
from .views import crystalsystem_detail,handpiece_detail, photograph_detail, mineraltype_detail
=======
from .views import crystalsystem_detail, handpiece_detail, photograph_detail, mineraltype_detail
from rest_framework.urlpatterns import format_suffix_patterns
>>>>>>> a05fe75... Created basic GET views, tests not working jet

app_name = "api"
urlpatterns = [

    # Detail Views for Crystalsystems, handpieces, Photographs and Mineraltypes

    url(r'^crystalsystem/(?P<pk>[0-9]+)/', crystalsystem_detail, name="crystalsystem"),

    url(r'^handpiece/(?P<pk>[0-9]+)/', handpiece_detail, name="handpiece"),

    url(r'photograph/(?P<pk>[0-9]+)/', photograph_detail, name="photograph"),

    url(r'mineraltype/(?P<pk>[0-9]+)/', mineraltype_detail, name="mineraltype"),

]
<<<<<<< HEAD
>>>>>>> 90d581e... Created apiurls in the right directory and edited the right urls,
=======
urlpatterns = format_suffix_patterns(urlpatterns)
>>>>>>> a05fe75... Created basic GET views, tests not working jet
