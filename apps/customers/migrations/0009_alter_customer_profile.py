# Generated by Django 5.0.1 on 2024-02-03 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_alter_customer_email_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile',
            field=models.ImageField(blank=True, default='./static/images/profile-user.jpeg', upload_to='profile/'),
        ),
    ]
