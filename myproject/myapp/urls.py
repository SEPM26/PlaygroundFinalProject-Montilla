from django.urls import path
from .views import index, galeria, contacto, agregar_producto

urlpatterns = [
    path('',index, name="index"),
    path ('galeria/', galeria, name="galeria"),
    path ('contacto/',contacto, name="contacto"),
    path ('agregar-producto/', agregar_producto, name="agregar_producto"),
]