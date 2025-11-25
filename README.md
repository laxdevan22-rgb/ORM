# Ex01 Django ORM Web Application
## Date: 

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import product,productAdmin
admin.site.register(product,productAdmin)
```
```

models.py
from django.db import models
from django.contrib import admin
class product(models.Model):
    serialNo=models.CharField(primary_key=True,max_length=8)
    productName=models.CharField(max_length=30)
    productId=models.CharField(max_length=16)
    ManufactureDate=models.CharField(max_length=15)
    deliverycharge=models.CharField(max_length=15)
    expiredate=models.CharField(max_length=15)
    price=models.CharField(max_length=15)
class productAdmin(admin.ModelAdmin):
    list_display = ["serialNo","productName","productId","ManufactureDate","deliverycharge","expiredate","price"]
```


## OUTPUT
<img width="1918" height="1078" alt="Screenshot 2025-11-25 114351" src="https://github.com/user-attachments/assets/83d5a10c-140e-48c4-902a-8059ba3f0441" />



## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
