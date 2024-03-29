# Generated by Django 4.0 on 2022-01-08 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omnicare', '0009_alter_patient_doctor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='patient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='omnicare.patient'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='nurse_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='omnicare.nurse'),
        ),
    ]
