from django.contrib import admin

from .models import tipounion
# Register your models here.
class tipounionAdimn(admin.ModelAdmin):
    search_fields=('union'),
    ordering=['union']

admin.site.register(tipounion,tipounionAdimn)

