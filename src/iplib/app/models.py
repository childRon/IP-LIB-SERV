from django.db import models

class ComponentDefinition(models.Model):
    title = models.CharField(max_length=30)
    short_name = models.CharField(max_length=10, blank=False, primary_key=True, verbose_name="Short Name")
    description = models.TextField()
    platform = models.CharField(max_length=20)
    editions = models.CharField(max_length=200)
    categories = models.ManyToManyField('Category')

    class Meta:
        unique_together = ('short_name', 'platform', 'editions')

    def __unicode__(self):
        return self.title

    
class VersionedComponent(models.Model):
    version_number = models.CharField(verbose_name="Version Number",max_length=10)
    author = models.CharField(max_length=50, blank=True)
    component = models.OneToOneField(ComponentDefinition, blank=False, verbose_name="Component Definition")
    suit_version = models.CharField(max_length=30)
    depending_codes = models.CharField(max_length=200)
    date_added = models.DateField()
    catalog = models.CharField(max_length=100,blank=False)

    class Meta:
        unique_together = [("component", "version_number")]

    def __unicode__(self):
        return '%s_%s_%s_%s' % (self.component.short_name, self.component.editions, self.version_number, self.component.platform)
 
        
class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    child_categories = models.ManyToManyField('self', symmetrical=False, blank=True)
    def __unicode__(self):
        return self.title
