# Generated by Django 5.0.1 on 2024-02-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0014_alter_customer_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
    ]
