from django.contrib import admin

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status') #from models.py class Item