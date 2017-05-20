from django.conf.urls import include, url
from .views import crystalsystem_detail,handpiece_detail, photograph_detail, mineraltype_detail

app_name = "api"
urlpatterns = [
    # Detail Views for Crystalsystems, handpieces, Photographs and Mineraltypes
    url(r'^crystalsystem/(?P<pk>\d+)', crystalsystem_detail, name="crystalsystem" ),

    url(r'^handpiece/(?P<pk>\d+)', handpiece_detail, name="handpiece"),

    url(r'photograph/(?P<pk>\d+)', photograph_detail, name="photograph"),

    url(r'mineraltype/(?P<pk>\d+)', mineraltype_detail, name="mineraltype"),

]
