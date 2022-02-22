
from django.contrib import admin
from django.forms.formsets import ORDERING_FIELD_NAME
from  .models import Programa
from django.contrib import admin



class ProgramaAdmin(admin.ModelAdmin):
    ordering=['id']
    autocomplete_fields=['tipoarea']


    






admin.site.register(Programa,ProgramaAdmin)
