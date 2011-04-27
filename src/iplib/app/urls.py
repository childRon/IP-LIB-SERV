from django.conf.urls.defaults import patterns, include, url
from iplib.app.views import *

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^components/$', all_components),
    url(r'^categories/$', all_categories),
    url(r'^component/([A-Za-z]+)/$', component),
    url(r'^component/([A-Za-z]+)/version/(\d+)/$', version),
    url(r'^category/(\d+)/$', category),
)
