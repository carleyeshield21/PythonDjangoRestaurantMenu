from django.shortcuts import render
from django.views import generic
from .models import Item

# Create your views here.
class MenuList(generic.ListView):
    queryset = Item.object.order_by('date_created') #imported from models.py, we can put a minus sign to reverse the order
    template_name = 'index.html' #will be created in the directory

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html' #will be created in the directory