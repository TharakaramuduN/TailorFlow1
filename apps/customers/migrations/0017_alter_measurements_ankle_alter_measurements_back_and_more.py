# Generated by Django 5.0.1 on 2024-02-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0016_alter_customer_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='ankle',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='back',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='calf',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='chest',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='hips',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='inseam',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='knee',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='neck',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='outseam',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='sleeve',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='thigh',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='waist',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='waistband',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
