from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
    # photos = models.ImageField(upload_to='images/', null=True)
    photos= ImageField(null=True)
    
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name=models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.name
        
class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name