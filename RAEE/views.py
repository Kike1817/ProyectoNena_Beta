# En el archivo views.py de tu aplicación
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AgregarEmpleadoForm, AgregarComputadoraForm
from .models import Empleados, Computadoras


def Home(request):
    return render(request, 'Home.html')


def agregar_empleado(request):
    if request.method == "POST":
        form = AgregarEmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/empleados/')
    else:
        form = AgregarEmpleadoForm()
    return render(request, 'agregar_empleado.html', {'form': form})


def agregar_computadora(request):
    if request.method == 'POST':
        form = AgregarComputadoraForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/computadoras/')
    else:
        form = AgregarComputadoraForm()
    return render(request, 'agregar_computadora.html', {'form': form})


def lista_empleados(request):
    empleados = Empleados.objects.all()
    context = {
        'empleados': empleados
    }
    return render(request, 'lista_empleados.html', context)


def lista_computadoras(request):
    computadoras = Computadoras.objects.all()

    context = {
        'computadoras': computadoras
    }

    return render(request, 'lista_computadoras.html', context)


def editar_empleado(request, empleado_id):
    if request.method == 'GET':
        empleado = get_object_or_404(Empleados, pk=empleado_id)
        form = AgregarEmpleadoForm(instance=empleado)
        return render(request, 'editar_empleado.html', {'empleado': empleado, 'form': form})
    else:
        try:
            empleado = get_object_or_404(Empleados, pk=empleado_id)
            form = AgregarEmpleadoForm(request.POST, instance=empleado)
            form.save()
            return redirect('lista_empleados')
        except ValueError:
            return render(request, 'editar_empleado.html', {'empleado': empleado, 'form': form, 'error': "Error actualizando Datos"})


def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleados, pk=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')


def editar_computadora(request, computadora_id):
    if request.method == 'GET':
        computadora = get_object_or_404(Computadoras, pk=computadora_id)
        form = AgregarComputadoraForm(instance=computadora)
        return render(request, 'editar_Computadora.html', {'computadora': computadora, 'form': form})
    else:
        try:
            computadora = get_object_or_404(Computadoras, pk=computadora_id)
            form = AgregarComputadoraForm(request.POST, instance=computadora)
            form.save()
            return redirect('lista_computadoras')
        except ValueError:
            return render(request, 'editar_Computadora.html', {'computadora': computadora, 'form': form, 'error': "Error actualizando Datos"})


def eliminar_computadora(request, computadora_id):
    computadora = get_object_or_404(Computadoras, pk=computadora_id)
    if request.method == 'POST':
        computadora.delete()
        return redirect('lista_computadoras')


# Pruebaaaaaaaa

def computadoras_disponibles(request):
    empleados = Empleados.objects.all()
    computadoras = Computadoras.objects.all()
    context = {
        'empleados': empleados,
        'computadoras': computadoras
    }
    return render(request, 'Computadoras_Disponibles.html', context)


def computadoras_asignadas(request):
    empleados = Empleados.objects.all()
    computadoras = Computadoras.objects.all()
    context = {
        'empleados': empleados,
        'computadoras': computadoras
    }
    return render(request, 'Computadoras_Asignadas.html', context)


def computadoras_a_d(request):
    empleados = Empleados.objects.all()
    computadoras = Computadoras.objects.all()
    context = {
        'empleados': empleados,
        'computadoras': computadoras
    }
    return render(request, 'Computadoras_A_D.html', context)
