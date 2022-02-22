from typing import Union
from django import forms


from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from  .models import Programa
from  applications.areas.models import areaslista



class ProgramaForm(forms.ModelForm):
   
    class Meta:
        model = Programa
        fields = (
            'Tramo',
            'Dfinal',
            'de1',
            'de2',
            'de3',
            'd1distancia',
            'Ntramo',
            'tipoarea',
            'Codigo',
            'Darea',
            'npersonas',
            'Unión',
        )
        labels = {
            'Tramo':'Tramo',
            'Dfinal':'Derivación final',
            'de1':'Derivación 1',
            'de2':'Derivación 2',
            'de3':'Derivación 3',
            'de1distancia':'Dinstacia del tramo',
            'Ntramo':'Número de codos por tramo',
            'tipoarea':'Tipo de área',
            'Codigo':'Código del área',
            'Darea':'Área [m2]',
            'npersonas':'Número de personas por area',
            'Unión':'Tipo de unión',

        } 


        widgets = {
            'Tramo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el Tramo'}),
            'Dfinal':forms.CheckboxInput(attrs={'class':'form-control'}),
            'de1':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la derivación 1'}),
            'de2':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la derivación 2'}),
            'de3':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la Derivación 3'}),
            'd1distancia':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la distancia en [m]'}),
            'Ntramo':forms.TextInput(attrs={'class':'form-control'}),
            'tipoarea':forms.Select(attrs={'class':'form-control'}),
            'Codigo':forms.TextInput(attrs={'class':'form-control'}),
            'Darea':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el área [m2]'}),
            'npersonas':forms.TextInput(attrs={'class':'form-control'}),
            'Unión':forms.Select(attrs={'class':'form-control'}),

        }





    
  

