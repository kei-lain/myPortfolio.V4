from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from datetime import datetime

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Project(models.Model):
    name = models.CharField(max_length=100)
    programmingLanguages = ArrayField(models.CharField(max_length=50) , default=list, blank=False)
    framework = ArrayField(models.CharField(max_length=50) , default=list, blank=False)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.URLField(max_length=300, blank= True)
    demonstrationVideo = models.URLField(max_length=300, blank= True)


    def __str__(self):
        return self.name