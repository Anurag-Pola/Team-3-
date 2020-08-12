from django.db import models
from accounts.models import Fpo

# Create your models here.


class Product(models.Model):
    productname = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    expectedprice = models.IntegerField(blank=True)
    datecreated = models.DateTimeField(auto_now_add= True)
    fpo = models.ForeignKey(Fpo,on_delete=models.CASCADE,related_name='product')



