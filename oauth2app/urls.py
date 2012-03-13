# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

from oauth2app import views
from oauth2app.token import handler

urlpatterns = patterns('',
    url(r'^missing_redirect_uri/$',
        views.MissingRedirectUriView.as_view(),
        name='missing_redirect_uri'),

    url(r'authorized/$',
        views.AuthorizeView.as_view(),
        name='authorize'),

    url(r'^token/$',
        handler,
        name='handler'),

)
