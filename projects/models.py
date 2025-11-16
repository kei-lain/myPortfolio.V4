from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from datetime import datetime

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class ProgrammingLanguage(models.Model):
    programming_language = models.CharField(max_length=50)
    def __str__(self):
        return self.programming_language
    
class Framework(models.Model):
    framework_name = models.CharField(max_length=100)
    def __str__(self):
        return self.framework_name



class Project(models.Model):
    name = models.CharField(max_length=100)
    programmingLanguages = models.ManyToManyField(ProgrammingLanguage)
    framework = models.ManyToManyField(Framework, blank=True)
    description = models.TextField(blank=False)
    category = models.ManyToManyField(Category)
    url = models.URLField(max_length=300, blank= True)
    demonstrationVideo = models.URLField(max_length=300, blank= True)


    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=False)
    publishingDate = models.DateTimeField()