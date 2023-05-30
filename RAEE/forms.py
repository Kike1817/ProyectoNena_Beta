# En el archivo forms.py de tu aplicación
from django import forms
from .models import Empleados, Computadoras


class AgregarEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ('cod_nomina', 'nombre', 'apellido', 'departamento', 'cargo')


class AgregarComputadoraForm(forms.ModelForm):
    class Meta:
        model = Computadoras
        fields = '__all__'


# Pruebaaaa
