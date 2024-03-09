from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.products.models import Product
from django.conf import settings
from pathlib import Path
import os

# Create your models here.

class TailorUser(AbstractUser):
    phone = models.CharField(max_length=15,blank=True, null=True,unique=True)
    profile = models.ImageField(blank=True,upload_to='tailor_profiles/',default='default/profile-user.png')
    email = models.EmailField(unique=True)

@receiver(post_save,sender=TailorUser)
def create_default_products(sender,instance,created,*args, **kwargs):
    if created:
        base_dir = str(settings.MEDIA_ROOT)
        image_dir = os.path.join(base_dir,'default', 'product_images')
        Product.objects.create(tailor=instance,title='Mens Casual Shirt',description='Casual shirt for mens',price=499,category='Shirt',image=os.path.join(image_dir,'mens_casual_shirt.jpg'),gender='M')
        Product.objects.create(tailor=instance,title='Mens Oversized Shirt',description='Oversized shirt for mens',price=699,category='Shirt',image=os.path.join(image_dir,'oversized_shirt.jpg'),gender='M')
        Product.objects.create(tailor=instance,title='Embroided Shirt',description='Embroided shirt for mens',price=699,category='Shirt',image=os.path.join(image_dir,'embroided_shirt_men.webp'),gender='M')
        Product.objects.create(tailor=instance,title='Formal Pant',description='Formal Pant for mens',price=699,category='Pant',image=os.path.join(image_dir,'mens_formal_pant.webp'),gender='M')
        Product.objects.create(tailor=instance,title='Embroided Shirt',description='Embroided shirt for women',price=699,category='Shirt',image=os.path.join(image_dir,'embroided_shirt_women.webp'),gender='F')
        Product.objects.create(tailor=instance,title='Tunic Shirt',description='Tunic shirt for women',price=699,category='Shirt',image=os.path.join(image_dir,'tunic_shirt_women.webp'),gender='F')
        Product.objects.create(tailor=instance,title='Oversized Shirt',description='Oversized shirt for women',price=699,category='Shirt',image=os.path.join(image_dir,'oversized_shirt_women.webp'),gender='F')
        Product.objects.create(tailor=instance,title='Formal Shirt',description='Formal Pant for women',price=699,category='Pant',image=os.path.join(image_dir,'women_pant.webp'),gender='F')