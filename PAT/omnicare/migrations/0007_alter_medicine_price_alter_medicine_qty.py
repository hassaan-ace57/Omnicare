# Generated by Django 4.0 on 2022-01-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnicare', '0006_alter_medicine_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='qty',
            field=models.IntegerField(null=True),
        ),
    ]
