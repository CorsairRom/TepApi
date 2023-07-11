from django.shortcuts import render

from api.serializers import SerializerEmpleados, SerializerEmpresas
from api.models import Empleados, Empresas

from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class EmpresasViewSet(viewsets.ModelViewSet):
    serializer_class = SerializerEmpresas
    queryset = Empresas.objects.all()
    
class EmpleadosViewSet(viewsets.ModelViewSet):
    serializer_class = SerializerEmpleados
    queryset = Empleados.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['empresa',]