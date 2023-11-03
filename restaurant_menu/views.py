from django.shortcuts import render
from django.views import generic
from .models import Item

# Create your views here.
class MenuList(generic.ListView):
    queryset = Item.object.order_by('date_created') #imported from models.py, we can put a minus sign to reverse the order

class MenuItemDetail(generic.DetailView):
    pass