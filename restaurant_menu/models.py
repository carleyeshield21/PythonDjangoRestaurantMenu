from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')
)
class Item(models.Model): #creating the columns in the table
    meal = models.CharField(max_length=1000, unique=True) #unique to avoid duplicate values
    description = models.CharField(max_length=2000) #no need to set unique because this variable can have duplicate values
    price = models.DecimalField(decimal_places=2)
    meal_type = models.CharField(choice=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if someone makes a meal, and if he is removed from the users, all his created items
    # will be deleted, or if you want to save the meals created, you should use the code models.PROTECT
