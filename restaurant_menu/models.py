from django.db import models

# Create your models here.
class Item(models.Model): #creating the columns in the table
    meal = models.CharField(max_length=1000, unique=True) #unique to avoid duplicate values
    description = models.CharField(max_length=1000) #no need to set unique because this variable can have duplicate values