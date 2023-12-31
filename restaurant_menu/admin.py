from django.contrib import admin
from .models import Item

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status') #from models.py class Item
    list_filter = ('status',) #a comma is necessary for python to read it as a tuple, otherwise it will result to an error
    search_fields = ('meal', 'description')

admin.site.register(Item, MenuItemAdmin) #to render the admin login page /admin