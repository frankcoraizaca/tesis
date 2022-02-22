from django.contrib import admin
from django.urls import path
from . import views
from applications import ventilcion

   
urlpatterns = [

    path('registro/', views.registroventi.as_view(),name='registro'),
    path('listaprograma/', views.listaListView.as_view()), 
    path('cambiar/<pk>/', views.ProgramadateView.as_view(), name= 'cambiar'),
    path('listaprograma/', views.listaListView.as_view(), name= 'listaprograma' ),
    path('objetivo/', views.suma, name= 'objetivo' ),
    path('informe/', views.informe, name= 'informe' ),
    path('velocidad/', views.Velocidad, name= 'velocidad' ),
    path('guardar/', views.guardar, name= 'guardar' ),
    path('cargar/', views.cargar, name= 'cargar' ),
    path('flujo/', views.flujorequerido, name= 'flujo' ),
    path('indice/', views.indice, name= 'indice'),
    path('tutorial/', views.download_file, name= 'tutorial'),
    path('eliminar/<pk>/', views.ProgramaDeleteView.as_view(), name= 'eliminar'),

  
]