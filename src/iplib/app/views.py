# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
# from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from iplib.app.models import ComponentDefinition, VersionedComponent, Category


def home(request):
        return render_to_response('home.html')
    
def all_components(request):
    components = VersionedComponent.objects.all()
    return render_to_response('all_components.html', {'components': components})

def all_categories(request):
    categories = Category.objects.all()
    return render_to_response('all_categories.html', {'categories': components})

def component(request, shortName):
    componentDefinition = ComponentDefinition.objects.filter(short_name=shortName)
    versions = VersionedComponent.objects.all().filter(component=componentDefinition)
    numbers = {}
    for version in versions:
        numbers.append(version.version_number)

    return render_to_response('component.html', {'version_numbers': numbers, 'component':componentDefinition})
    
def version(request, shortName, version_id):
    try:
       version_id = int(version_id)
    except ValueError:
        raise Http404()
    versionedComponent = VersionedComponent.objects.get(id=version_id)
    component = versionedComponent.component;
    return render_to_response('versionedComponent.html', {'versioned_component': versionedComponent, 'component':component})

def category(request, category_id):
    try:
       category_id = int(category_id)
    except ValueError:
        raise Http404()
        category = Category.objects.get(id=category_id)
    return render_to_response('category.html', {'category': category})


