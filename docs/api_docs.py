from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework import permissions
from django.urls import reverse
import environ

# This is the documentation for the API, generated for swagger and Redoc standart
env = environ.Env()
base_url = "https://{}/api".format(env("DJANGO_ALLOWED_HOSTS", default="localhost:8000"))

schema_view = get_schema_view(
    openapi.Info(
        title="GeoMat API",
        default_version='v1.0',
        description="This is the API for the elearning project GeoMat",
        contact=openapi.Contact(email="christian@elearning.physik.uni-frankfurt.de"),
    ),
   # validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=base_url, # hard coded for now
)
app_name = "api_docs"
urlpatterns = [
    url(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]
