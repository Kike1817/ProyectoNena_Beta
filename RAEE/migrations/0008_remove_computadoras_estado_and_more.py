# Generated by Django 4.2 on 2023-05-25 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RAEE', '0007_computadoras_empleado_asignado_computadoras_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computadoras',
            name='estado',
        ),
        migrations.AlterField(
            model_name='computadoras',
            name='fecha_asignacion',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
