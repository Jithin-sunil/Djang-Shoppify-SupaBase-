from django.db import models
from Admin.models import *


class tbl_user(models.Model):
    user_id = models.TextField(primary_key=True,  editable=False)  
    user_name = models.CharField(max_length=50, unique=True)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=255)
    user_photo = models.URLField()
    user_contact = models.CharField(max_length=50)
    user_address = models.CharField(max_length=255)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)


class tbl_shop(models.Model):
    shop_id = models.CharField(primary_key=True)
    shop_name = models.CharField(max_length=50, unique=True)
    shop_email = models.EmailField(unique=True)
    shop_password = models.CharField(max_length=255)
    shop_photo=models.URLField()
    shop_contact = models.CharField(max_length=50)
    shop_address = models.CharField(max_length=255)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE) 

