# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
# from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from iplib.app.models import ComponentDefinition, VersionedComponent, Category


def home(request):
        return render_to_response('home.html')
    
def all_components(request):
    
    html = "все компоненты"
    return HttpResponse(html)
    
def all_categories(request):
    html = "Все Категории"
    return HttpResponse(html)

def component(request, component_id):
    html = "Какой-то компонент"
    return HttpResponse(html)
    
def version(request, component_id, version_id):
    html = "Какая-то версия"
    return HttpResponse(html)
    
def category(request, category_id):

    html = "Какая-то категория"
    return HttpResponse(html)


