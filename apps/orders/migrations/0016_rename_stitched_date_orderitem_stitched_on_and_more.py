# Generated by Django 5.0.1 on 2024-02-25 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_order_items_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='stitched_date',
            new_name='stitched_on',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='is_delivered',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='delivered_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(blank=True, choices=[('Not Stitched', 'Not Stitched'), ('Stitching', 'Stitching'), ('Delivered', 'Delivered'), ('Stitched', 'Stitched')], default='Not Stitched', max_length=100, null=True),
        ),
    ]