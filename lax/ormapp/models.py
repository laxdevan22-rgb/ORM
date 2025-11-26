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
 