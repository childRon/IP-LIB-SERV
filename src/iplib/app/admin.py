from django.contrib import admin
from iplib.app.models import ComponentDefinition, VersionedComponent, Category

admin.site.register(ComponentDefinition)
admin.site.register(VersionedComponent)
admin.site.register(Category)
