# Generated by Django 5.0.1 on 2024-02-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailors', '0002_tailoruser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tailoruser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]