from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name = models.CharField(max_length=50)

class tbl_place(models.Model):
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name = models.CharField(max_length=50)


class tbl_subcategory(models.Model):
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50)
