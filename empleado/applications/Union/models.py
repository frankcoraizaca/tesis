from django.db import models

# Create your models here.
class tipounion(models.Model):
   union = models.CharField('unión', max_length=60)
   class Meta: 
      verbose_name= 'tipounion'
      verbose_name_plural= 'tipounion'
   
   
   def __str__(self):
        return self.union