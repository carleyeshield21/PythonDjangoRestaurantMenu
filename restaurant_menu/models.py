from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available'),
)

class Item(models.Model): #creating the columns in the table
    meal = models.CharField(max_length=1000, unique=True) #unique to avoid duplicate values
    description = models.CharField(max_length=2000) #no need to set unique because this variable can have duplicate values
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200,choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT) #if an author makes a meal, and if he is removed from the users, all his created items
    # will be deleted, or if you want to save the meals created, you should use the code models.PROTECT, if you use models.SET_NULL,
    # the items or meals will be retained but the author will be set to a no value, if the author is deleted
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now=True) #will generated date-time stamps whenever a meal is created
    date_updated = models.DateTimeField(auto_now=True) #will generated date-time stamps whenever a meal is created

    def __str__(self):
        return self.meal