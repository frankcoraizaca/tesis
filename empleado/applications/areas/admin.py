from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import areaslista
# Register your models here.

class areaslistaAdimn(admin.ModelAdmin):
    search_fields=('areas'),
    ordering=['areas']


admin.site.register(areaslista, areaslistaAdimn)
