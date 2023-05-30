from django.contrib import admin
from .models import Computadoras, Empleados


class ComputadorasAdmin(admin.ModelAdmin):
    # nombres de los atributos en el modelo
    list_display = ('serial', 'modelo', 'actualizada')


admin.site.register(Computadoras, ComputadorasAdmin)


class EmpleadosAdmin(admin.ModelAdmin):
    # nombres de los atributos en el modelo
    list_display = ('cod_nomina', 'nombre', 'cargo')


admin.site.register(Empleados, EmpleadosAdmin)

