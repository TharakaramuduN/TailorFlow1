from django.db import models
from apps.tailors.models import TailorUser
# from orders.models import Order
# from transactions.models import Transaction
# Create your models here. 

class Customer(models.Model):
    tailor = models.ForeignKey(TailorUser,on_delete=models.CASCADE,null=True,blank=True)
    # orders = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    # transactions = models.ForeignKey(Transaction,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(blank=False)
    city = models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=20,blank=False)
    profile = models.ImageField(blank=True,null=True,upload_to='profile/',default='profile/profile-user.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name

class Measurements(models.Model):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)
    neck = models.FloatField(null=True, blank=True)
    chest = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    hips = models.FloatField(null=True, blank=True)
    thigh = models.FloatField(null=True, blank=True)
    knee = models.FloatField(null=True, blank=True)
    calf = models.FloatField(null=True, blank=True)
    sleeve = models.FloatField(null=True, blank=True)
    back = models.FloatField(null=True, blank=True)
    waistband = models.FloatField(null=True, blank=True)
    outseam = models.FloatField(null=True, blank=True)
    inseam = models.FloatField(null=True, blank=True)
    ankle = models.FloatField(null=True, blank=True)