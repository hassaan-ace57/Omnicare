# Generated by Django 4.0 on 2022-01-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnicare', '0005_alter_medicine_manu_alter_medicine_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.IntegerField(),
        ),
    ]