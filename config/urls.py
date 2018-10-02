# -*- coding: utf-8 -*-
"""URLs for geomat project"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views import defaults as default_views
from django.views.generic import RedirectView
from geomat.stein.views import gallery_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^$', gallery_view, name="home"),
    # Redirect users from outdated 'preview/' to '/'
    url(r'^preview/', RedirectView.as_view(pattern_name='home')),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # REST framework
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include("geomat.stein.apiurls", namespace="api")),

    # Let's fix this stupid issue with Google Chrome and make a redirect from '/favicon.ico' to our
    # 'common/images/favicon.ico' file!
    # Google Chrome ignores the favicon file defined in HTML and always looks for it in '/favicon.ico'
    url(r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('common/images/favicon.ico'),
            permanent=False),
        name="favicon"),
    url(r'^gallery/', gallery_view, name="gallery_listview"),

    # Do some redirects to the correct URL, as some people manage to get typos in
    url(r'^galery/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^galerie/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^gallerie/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^garllry/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^garllery/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^galary/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^gallary/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^gallarie/', RedirectView.as_view(pattern_name='gallery_listview')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$',
            default_views.bad_request,
            kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$',
            default_views.permission_denied,
            kwargs={'exception': Exception("Permissin Denied")}),
        url(r'^404/$',
            default_views.page_not_found,
            kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

# Check for the rosetta module in local installation
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]
