from django.contrib import admin
from ostis.iplib.models import Component, Edition, Version, Category

admin.site.register(Component)
admin.site.register(Edition)
admin.site.register(Version)
admin.site.register(Category)