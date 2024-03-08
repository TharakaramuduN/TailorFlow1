# Generated by Django 5.0.1 on 2024-02-10 07:50

from django.db import migrations, models
from apps.products.models import Product
from django.conf import settings

def create_default_products():
    Product.objects.create(title='Mens Casual Shirt',description='Casual shirt for mens',price=499,category='Shirt',image=settings.BASE_DIR+'media/default/product_images/mens_casual_shirt.jpg',gender='M')
    Product.objects.create(title='Mens Oversized Shirt',description='Oversized shirt for mens',price=699,category='Shirt',image=settings.BASE_DIR+'media/default/product_images/oversized_shirt.jpg',gender='M')
    Product.objects.create(title='Embroided Shirt',description='Embroided shirt for mens',price=699,category='Shirt',image=settings.BASE_DIR+'media/default/product_images/embroided_shirt_men.webp',gender='M')
    Product.objects.create(title='Formal Pant',description='Formal Pant for mens',price=699,category='Pant',image=settings.BASE_DIR+'media/default/product_images/mens_formal_pant.webp',gender='M')
    Product.objects.create(title='Embroided Shirt',description='Embroided shirt for women',price=699,category='Shirt',image=settings.BASE_DIR+'media/default/product_images/embroided_shirt_women.webp',gender='F')
    Product.objects.create(title='Tunic Shirt',description='Tunic shirt for women',price=699,category='Shirt',image=settings.BASE_DIR+'media/default/product_images/tunic_shirt_women.webp',gender='F')
    Product.objects.create(title='Oversized Shirt',description='Oversized shirt for women',price=699,category='Shirt',image=settings.BASE_DIR+'media/default/product_images/oversized_shirt_women.webp',gender='F')
    Product.objects.create(title='Formal Shirt',description='Formal Pant for women',price=699,category='Pant',image=settings.BASE_DIR+'media/default/product_images/women_pant.webp',gender='F')

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.RunPython(create_default_products),
    ]
