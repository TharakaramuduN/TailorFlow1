from django.db import models
from apps.tailors.models import TailorUser
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os
from django.conf import settings
# from orders.models import Order
# from transactions.models import Transaction
# Create your models here. 

class Customer(models.Model):
    gender_choices = [
        ('M',"Male"),
        ('F',"Female"),
    ]
    tailor = models.ForeignKey(TailorUser,on_delete=models.CASCADE,blank=True)
    # orders = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    # transactions = models.ForeignKey(Transaction,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(blank=False)
    gender = models.CharField(max_length=1,choices=gender_choices)
    city = models.CharField(max_length=50,blank=False)
    phone = models.CharField(max_length=20,blank=False)
    profile = models.ImageField(blank=True,null=True,upload_to='profile/',default='default/profile-user.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name
    
@receiver(pre_delete,sender=Customer)
def delete_profile_images(sender,instance,*args, **kwargs):
    image_path = instance.profile.path
    if instance.profile and image_path != os.path.join(settings.BASE_DIR, 'media', 'default', 'profile-user.png'):
        if os.path.exists(image_path):
            os.remove(image_path)
                


class Measurements(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)
    neck = models.FloatField(null=True, blank=True,default=0)
    chest = models.FloatField(null=True, blank=True,default=0)
    waist = models.FloatField(null=True, blank=True,default=0)
    hips = models.FloatField(null=True, blank=True,default=0)
    thigh = models.FloatField(null=True, blank=True,default=0)
    knee = models.FloatField(null=True, blank=True,default=0)
    calf = models.FloatField(null=True, blank=True,default=0)
    sleeve = models.FloatField(null=True, blank=True,default=0)
    back = models.FloatField(null=True, blank=True,default=0)
    waistband = models.FloatField(null=True, blank=True,default=0)
    outseam = models.FloatField(null=True, blank=True,default=0)
    inseam = models.FloatField(null=True, blank=True,default=0)
    ankle = models.FloatField(null=True, blank=True,default=0)

    def __str__(self) -> str:
        return self.customer.first_name