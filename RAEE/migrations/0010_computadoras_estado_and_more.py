# Generated by Django 4.2.1 on 2023-05-25 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RAEE', '0009_alter_computadoras_empleado_asignado'),
    ]

    operations = [
        migrations.AddField(
            model_name='computadoras',
            name='estado',
            field=models.CharField(choices=[('AS', 'Asignado'), ('NA', 'No asignado')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='computadoras',
            name='empleado_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RAEE.empleados'),
        ),
    ]
