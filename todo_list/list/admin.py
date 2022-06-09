from django.contrib import admin

from .models import Item

class ListAdmin(admin.ModelAdmin): 
    pass





# Register your models here.
admin.site.register(Item, ListAdmin)