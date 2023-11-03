from django.shortcuts import render
from django.views import generic
from .models import Item
from .models import Item, MEAL_TYPE #from models.py

# Create your views here.
class MenuList(generic.ListView):
    queryset = Item.objects.order_by('date_created') #imported from models.py, we can put a minus sign to reverse the order
    template_name = 'index.html' #will be created in the project directory which must be named 'templates', this line also connects the html file
    # to the view, we must also make sure we go to the mysite directory, open settings.py and include 'templates' inside the TEMPLATES list inside
    # the 'DIRS' value, or you can transfer the templates folder inside the restaurant_menu

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        context['meals'] = MEAL_TYPE
        return context
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = {'meals': ['Pecha Pie','Ispa-getti', 'friends pry'],
    #                        'sangkap': ['mga', 'ingredients sa', 'pagluluto']
    #                      }
    #     return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html' #will be created in the directory