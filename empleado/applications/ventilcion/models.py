from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from  applications.areas.models import areaslista
from  applications.Union.models import tipounion
# Create your models here.

class Programa(models.Model): 

   Tramo = models.CharField('Tramo', max_length=50) 
   Dfinal= models.BooleanField('Derivación final',default=False)
   de1= models.CharField('Derivación 1', max_length=4,blank=True)
   de2= models.CharField('Derivación 2', max_length=4,blank=True)
   de3= models.CharField('Derivación 3', max_length=4,blank=True)
   d1distancia = models.FloatField('Distancia del tramo[m]',blank=True)
   Ntramo = models.IntegerField('Número de codos por tramo',null=True, blank=True)
   tipoarea =  models.ForeignKey(areaslista,null=True, blank=True, on_delete = models.CASCADE  )
   Codigo= models.CharField('Codigo', max_length=50,blank=True) 
   Darea = models.FloatField('área[m2]',max_length=4, null=True, blank=True)
   npersonas = models.IntegerField('Número de personas',null=True, blank=True)
   Unión = models.ForeignKey(tipounion,null=True, blank=True, on_delete = models.CASCADE  )

   def __str__(self):
        return "{}-{}-{}-{}-{}-{}".format (self.Tramo, self.Dfinal,self.de1, self.de2,self.de3,self.d1distancia,
         self. Ntramo,self. tipoarea, self.Codigo,self.Darea,self. npersonas, self.Unión )
