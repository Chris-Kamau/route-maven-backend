from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Todo(models.Model):
    number_plate = models.CharField(max_length=120)
    image = models.CharField(max_length=2000)
    driver_name = models.CharField(max_length=120)
    driver_contact = models.IntegerField(default=0)
    route = models.CharField(max_length=120, default="")
    gender = models.CharField(max_length=120, default="")
    
    class Meta:  
        db_table = "car" 



class Staff(models.Model):
    username = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200)
    password_confirmation = models.CharField(max_length=200)

    class Meta:
        db_table = "users"

   
   
   
   
    
    