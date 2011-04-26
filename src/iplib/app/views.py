# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
# from django.template import Context
from django.http import HttpResponse, Http404
from iplib.app.models import Component, Edition, Version, Category


def home(request):
    return render_to_response('home.html')
    
def all_components(request):
    components = Component.objects.all()
    return render_to_response('all_components.html', {'components': components})
    
def all_categories(request):
    categories = Category.objects.all()
    return render_to_response('all_categories.html', {'categories': categories})
    
def component(request, component_id):
    try:
        component_id = int(component_id)
    except ValueError:
        raise Http404()
    #html = "Какой-то компонент №%s" % component_id
    component = Component.objects.get(id=component_id)
    editions = component.edition_set.all()
    tuples = []
    for edition in editions:
        tuples.append((edition, edition.version_set.all()))
    return render_to_response('component.html', {'component': component, 'tuples': tuples})
    
def version(request, component_id, version_id):
    try:
        component_id = int(component_id)
        version_id = int(version_id)
    except ValueError:
        raise Http404()
    html = "Какая-то версия №%s компонента №%s" % (version_id, component_id)
    return HttpResponse(html)
    
def category(request, category_id):
    try:
        category_id = int(category_id)
    except ValueError:
        raise Http404()
    html = "Какая-то категория №%s" % category_id
    return HttpResponse(html)


