from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm, ProductoForm

# Create your views here.

def index(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
         }

    return render(request, 'myapp/index.html', data)

def galeria(request):

    return render(request, 'myapp/galeria.html')

def contacto(request):
    data = {
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "contacto guardado"

        else:
            data ["form"] = formulario

    return render(request, 'myapp/contacto.html', data)

def agregar_producto (request):

    data = {
        'form': ProductoForm()
    }
    
    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'myapp/producto/agregar.html', data)
      
      





