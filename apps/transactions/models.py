from django.db import models
from apps.orders.models import Order
from apps.tailors.models import TailorUser

# Create your models here.
class Transaction(models.Model):
    tailor = models.ForeignKey(TailorUser,on_delete = models.CASCADE,blank=True,null=True)
    amount = models.FloatField(blank=True,null=True,default=0)
    date_time = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        ordering = ['-id']
