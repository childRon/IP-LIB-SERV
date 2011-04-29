from django.conf.urls.defaults import patterns, include, url
from iplib.app.views import *
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^components/$', all_components),
    url(r'^categories/$', all_categories),
    url(r'^component/([A-Za-z]+)/$', component),
    url(r'^component/([A-Za-z]+)/version/([\d*[.]+]*)/$', version),
    url(r'^category/(\d+)/$', category),
    url(r'^component/[A-Za-z]+/category/(\d+)/$', category),
    url(r'^component/[A-Za-z]+/version/[\d*[.]+]*/category/(\d+)/$', category),
    )

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        (r'^static_media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
