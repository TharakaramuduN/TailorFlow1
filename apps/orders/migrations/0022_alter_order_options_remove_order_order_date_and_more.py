# Generated by Django 5.0.1 on 2024-03-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_alter_order_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-order_date_time']},
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.AddField(
            model_name='order',
            name='order_date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
