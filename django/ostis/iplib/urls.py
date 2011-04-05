from django.conf.urls.defaults import patterns, include, url
from ostis.iplib.views import *

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^components/$', all_components),
    url(r'^categories/$', all_categories),
    url(r'^component/(\d+)/$', component),
    url(r'^component/(\d+)/version/(\d+)/$', version),
    url(r'^category/(\d+)/$', category),
)
