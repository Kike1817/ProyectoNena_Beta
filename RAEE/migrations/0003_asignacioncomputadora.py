# Generated by Django 4.2.1 on 2023-05-23 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RAEE', '0002_alter_computadoras_serial_alter_empleados_cod_nomina'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionComputadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignada', models.BooleanField(default=False)),
                ('fecha_asignacion', models.DateField(auto_now_add=True)),
                ('computadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RAEE.computadoras')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RAEE.empleados')),
            ],
        ),
    ]