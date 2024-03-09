from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os

# Create your models here.

class Product(models.Model):
    gender_choices = [
        ('M','Male'),
        ('F','Female')
    ]
    tailor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    inventory = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/')
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=50,choices=gender_choices,null=True)

    def __str__(self) -> str:
        return self.title

receiver(pre_delete,sender=Product)
def delete_product_images(instance,*args, **kwargs):
    if instance.image:
        if os.path.exists(instance.image.path):
            os.remove(instance.image.path)