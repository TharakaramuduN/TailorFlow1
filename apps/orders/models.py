from django.db import models
from apps.customers.models import Customer
from apps.tailors.models import TailorUser
from apps.products.models import Product
import datetime
# Create your models here.
class Order(models.Model):
    payment_choices = [
        ('PRE','PREPAID'),
        ('POST','POSTPAID')
    ]
    tailor = models.ForeignKey(TailorUser,on_delete=models.CASCADE,null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    order_date = models.DateField(auto_now_add=True,blank=True,null=True)
    total_price = models.IntegerField(blank=True,null=True)
    payment_type = models.CharField(max_length=50,choices=payment_choices,null=True)



class OrderItem(models.Model):
    status_choices=[
        ('Not Stitched','Not Stitched'),
        ('Stitching','Stitching'),
        ('Stitched',"Stitched")
    ]
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING,null=True)
    notes = models.TextField(max_length=200,blank=True,null=True)
    quantity = models.PositiveIntegerField(default=1)
    requested_date = models.DateField()
    status = models.CharField(max_length=100,choices=status_choices,default="Not Stitched",blank=True,null=True)
    urgent = models.BooleanField(default=False,blank=True)