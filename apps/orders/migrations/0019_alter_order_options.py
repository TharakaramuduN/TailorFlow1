# Generated by Django 5.0.1 on 2024-03-02 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-id']},
        ),
    ]
