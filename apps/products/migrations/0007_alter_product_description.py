# Generated by Django 5.0.1 on 2024-02-10 07:50

from django.db import migrations, models

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
    ]
