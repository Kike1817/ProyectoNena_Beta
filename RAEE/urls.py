from django.urls import path
from RAEE import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="Home"),
    path('empleados/', views.agregar_empleado, name="agregar_empleado"),
    path('empleados/lista/', views.lista_empleados, name='lista_empleados'),
    path('empleados/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/<int:empleado_id>/eliminar', views.eliminar_empleado, name='eliminar_empleado'),

    path('computadoras/', views.agregar_computadora, name="agregar_computadora"),
    path('computadoras/lista/', views.lista_computadoras, name='lista_computadoras'),
    path('computadoras/<int:computadora_id>/', views.editar_computadora, name='editar_computadora'),
    path('computadoras/<int:computadora_id>/eliminar', views.eliminar_computadora, name='eliminar_computadora'),

    path('computadoras/asignadas/', views.computadoras_asignadas, name="computadoras_asignadas"),
    path('computadoras/disponibles/', views.computadoras_disponibles, name="computadoras_disponibles"),
    path('computadoras/a/d/', views.computadoras_a_d, name="computadoras_a_d"),
]
