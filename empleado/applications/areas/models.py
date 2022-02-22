from django.db import models

# Create your models here.
class areaslista(models.Model):
    areas= models.CharField('tipo de Areas', max_length=60,null=True,blank=True) 
    listrosporpersona = models.FloatField('L/s personas',max_length=4, null=True, blank=True)
    litrosporarea = models.FloatField('L/s area',max_length=4, null=True, blank=True)  
    def __str__(self):
        return "{}-{}".format (self.areas, self.listrosporpersona,self.litrosporarea)
