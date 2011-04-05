from django.db import models

class Component(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    
    def __unicode__(self):
        return self.title
    
    
class Edition(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    component = models.ForeignKey(Component)
    
    def __unicode__(self):
        return '%s %s' % (self.component.title, self.title)
    
    
class Version(models.Model):
    number = models.CharField(max_length=10)
    description = models.CharField(max_length=150)
    component = models.ForeignKey(Component)
    edition = models.ForeignKey(Edition)
    suit_version = models.CharField(max_length=30)
    dependence = models.CharField(max_length=150)
    date_added = models.DateField()
    download_link = models.URLField()
    
    def __unicode__(self):
        return '%s %s %s' % (self.component.title, self.edition.title, self.number)
        
        
class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    component_versions = models.ManyToManyField(Version)
    
    def __unicode__(self):
        return self.title

