# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views import defaults as default_views
from django.views.generic import RedirectView, TemplateView

from geomat.stein.views import GalleryListView

urlpatterns = [
    url(r'^$', GalleryListView.as_view(), name="home"),
    # url(r'^preview$', TemplateView.as_view(template_name='pages/preview.html'), name="preview"),
    # url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include("geomat.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here

    # Let's fix this stupid issue with Google Chrome and make a redirect from /favicon.ico to our /img/favicon.ico file!
    # Google Chrome ignores the favicon file defined in HTML and always looks for it in /
    url(
        r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('common/images/favicon.ico'),
            permanent=False),
        name="favicon"
    ),
    url(r'^gallery/', RedirectView.as_view(url='/#gallery'), name="gallery_listview"),

    # Do some redirects to the correct URL, as some people manage to get typos in
    url(r'^galery/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^galerie/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^gallerie/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^garllry/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^garllery/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^galary/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^gallary/', RedirectView.as_view(pattern_name='gallery_listview')),
    url(r'^gallarie/', RedirectView.as_view(pattern_name='gallery_listview')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
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
