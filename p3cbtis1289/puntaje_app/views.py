from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,"index.html")

def proveedores(request):
    return render(request,"proveedores.html")

def empleados(request):
    return render(request,"empleado.html")

def sucursal(request):
    return render(request,"sucursal.html")

def tabla_clientes(request):
    return render(request,"tabla_clientes.html")