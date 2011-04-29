# -*- coding: utf-8 -*-
import glob
from django.shortcuts import render_to_response
# from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from iplib.app.models import ComponentDefinition, VersionedComponent, Category
import os, tempfile, zipfile
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.conf import settings

def home(request):
        return render_to_response('home.html')
    
def all_components(request):
    components = VersionedComponent.objects.all()
    return render_to_response('all_components.html', {'components': components})

def all_categories(request):
    categories = Category.objects.all()
    return render_to_response('all_categories.html', {'categories': categories})

def component(request, shortName):
    componentDefinition = ComponentDefinition.objects.get(short_name=shortName)
    versions = VersionedComponent.objects.all().filter(component=componentDefinition)
    numbers = []
    for version in versions:
        numbers.append(version.version_number)
    return render_to_response('component.html', {'version_numbers': numbers, 'component':componentDefinition})
    
def version(request, shortName, number):
    componentDefinition = ComponentDefinition.objects.get(short_name=shortName);
    versionedComponent = VersionedComponent.objects.get(version_number=number, component = componentDefinition)
    return render_to_response('component.html', {'versioned_component': versionedComponent, 'component':componentDefinition})

def category(request, category_id):
    try:
       category_id = int(category_id)
       category = Category.objects.get(id=category_id)
    except ValueError:
        raise Http404()

    return render_to_response('category.html', {'category': category})

def download(request, shName, versionNumber):

    catalog_path = settings.CATALOG_IPCOMPONENTOV
    componentDefinition = ComponentDefinition.objects.get(short_name=shName);
    code_name = componentDefinition.short_name +"_"+ componentDefinition.editions +"_"+ versionNumber +"_"+ componentDefinition.platform;

    full_path = catalog_path + "/" + code_name

    filename = code_name + '.zip'
    directory = full_path
#    temp = createZipFile(filename,[],directories)
    temp = zipdir(directory,filename)
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response


def zipdir(dirPath=None, zipFilePath=None, includeDirInZip=True):
    temp = tempfile.TemporaryFile()
    if not zipFilePath:
        zipFilePath = dirPath + ".zip"
    if not os.path.isdir(dirPath):
        raise OSError("dirPath argument must point to a directory. "
            "'%s' does not." % dirPath)
    parentDir, dirToZip = os.path.split(dirPath)
    #Little nested function to prepare the proper archive path
    def trimPath(path):
        archivePath = path.replace(parentDir, "", 1)
        if parentDir:
            archivePath = archivePath.replace(os.path.sep, "", 1)
        if not includeDirInZip:
            archivePath = archivePath.replace(dirToZip + os.path.sep, "", 1)
        return os.path.normcase(archivePath)

    outFile = zipfile.ZipFile(temp, "w",
        compression=zipfile.ZIP_DEFLATED)
    for (archiveDirPath, dirNames, fileNames) in os.walk(dirPath):
        for fileName in fileNames:
            filePath = os.path.join(archiveDirPath, fileName)
            outFile.write(filePath, trimPath(filePath))
        #Make sure we get empty directories as well
        if not fileNames and not dirNames:
            zipInfo = zipfile.ZipInfo(trimPath(archiveDirPath) + "/")
            #some web sites suggest doing
            #zipInfo.external_attr = 16
            #or
            #zipInfo.external_attr = 48
            #Here to allow for inserting an empty directory.  Still TBD/TODO.
            outFile.writestr(zipInfo, "")
    outFile.close()
    return temp
