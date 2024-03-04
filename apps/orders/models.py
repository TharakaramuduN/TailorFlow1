from django.db import models
from apps.customers.models import Customer
from apps.tailors.models import TailorUser
from apps.products.models import Product
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime
# Create your models here.
class Order(models.Model):
    payment_choices = [
        ('PRE','PREPAID'),
        ('POST','POSTPAID')
    ]
    id = models.CharField(max_length=100,primary_key=True,unique=True,blank=True)
    tailor = models.ForeignKey(TailorUser,on_delete=models.CASCADE,null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    order_date_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    total_price = models.FloatField(blank=True,null=True)
    payment_type = models.CharField(max_length=50,choices=payment_choices,null=True)
    items_count = models.IntegerField(blank=True,null=True)
    
    class Meta:
        ordering = ['-order_date_time']



class OrderItem(models.Model):
    status_choices=[
        ('Not-Stitched','Not-Stitched'),
        ('Stitching','Stitching'),
        ('Delivered','Delivered'),
        ('Stitched',"Stitched")
    ]
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING,null=True)
    notes = models.TextField(max_length=200,blank=True,null=True)
    quantity = models.PositiveIntegerField(default=1)
    requested_date = models.DateField()
    status = models.CharField(max_length=100,choices=status_choices,default="Not-Stitched",blank=True,null=True)
    urgent = models.BooleanField(default=False,blank=True)
    stitched_on = models.DateField(blank=True,null=True)
    delivered_on = models.DateField(blank=True,null=True)
