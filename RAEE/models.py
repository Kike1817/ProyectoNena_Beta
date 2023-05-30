from django.utils import timezone
from django.db import models


class Empleados(models.Model):
    opciones_departamentos = [
        ('S', 'Sistemas'),
        ('P', 'Presidencia'),
    ]
    opciones_cargos = [
        ('J', 'Jefe'),
        ('A', 'Administrador'),
    ]
    cod_nomina = models.CharField(max_length=4, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    departamento = models.CharField(
        max_length=1, choices=opciones_departamentos)
    cargo = models.CharField(max_length=1, choices=opciones_cargos)

    def __str__(self):
        return f"{self.cod_nomina} {self.nombre} {self.departamento}"


class Computadoras(models.Model):
    opciones_tipo_disco = [
        ('M2', 'M.2'),
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
    ]
    opciones_capacidad_disco = [
        ('32', '32gb'),
        ('64', '64gb'),
        ('128', '128gb'),
        ('256', '256gb'),
        ('512', '512gb'),
        ('1024', '1024gb'),
    ]
    opciones_tipo_ram = [
        ('DDR', 'DDR'),
        ('DDR2', 'DDR2'),
        ('DDR3', 'DDR3'),
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5'),
    ]
    opciones_memoria1_ram = [
        ('4', '4gb'),
        ('8', '8gb'),
        ('16', '16gb'),
        ('32', '32gb'),
        ('64', '64gb'),
    ]
    opciones_memoria2_ram = [
        ('4', '4gb'),
        ('8', '8gb'),
        ('16', '16gb'),
        ('32', '32gb'),
        ('64', '64gb'),
    ]
    opciones_procesador = [
        ('I3', 'i3'),
        ('I5', 'i5'),
        ('I7', 'i7'),
        ('C2D', 'Core2Duo'),
        ('ADM', 'ADM'),
        ('OTROS', 'OTROS...'),
    ]
    opciones_actualizada = [
        ('SI', 'SI'),
        ('NO', 'NO'),
    ]
    
    serial = models.CharField(max_length=4, unique=True)
    modelo = models.CharField(max_length=100)
    tipo_disco = models.CharField(max_length=3, choices=opciones_tipo_disco)
    capacidad_disco = models.CharField(
        max_length=4, choices=opciones_capacidad_disco)
    tipo_ram = models.CharField(max_length=4, choices=opciones_tipo_ram)
    memoria1_ram = models.CharField(
        max_length=2, choices=opciones_memoria1_ram)
    memoria2_ram = models.CharField(
        max_length=2, choices=opciones_memoria2_ram)
    procesador = models.CharField(max_length=7, choices=opciones_procesador)
    actualizada = models.CharField(max_length=2, choices=opciones_actualizada)
    fecha_asignacion = models.DateField(null=True)
    empleado_asignado = models.ForeignKey(
        Empleados, on_delete=models.SET_NULL, null=True, blank=True)
    asignado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.serial} {self.modelo} {self.actualizada}"


# Pruebaaaaa
