from django.contrib import admin
from .models import Category , Project , Framework, ProgrammingLanguage, Blog

# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Framework)
admin.site.register(ProgrammingLanguage)
admin.site.register(Blog)

