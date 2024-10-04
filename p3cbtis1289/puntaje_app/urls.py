from  django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("proveedores/",views.proveedores,name="proveedores"),
    path("empleados/",views.empleados,name="empleados"),
    path("sucursal/",views.sucursal,name="sucursal"),
    path("tabla_clientes/",views.tabla_clientes,name="tabla_clientes"),

]
