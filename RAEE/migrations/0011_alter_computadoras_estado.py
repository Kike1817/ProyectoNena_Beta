# Generated by Django 4.2.1 on 2023-05-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAEE', '0010_computadoras_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadoras',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
