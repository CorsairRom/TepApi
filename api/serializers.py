from rest_framework import serializers

from api.models import Empleados, Empresas


class SerializerEmpresas(serializers.ModelSerializer):
    
    class Meta:
        model = Empresas
        fields = '__all__'

class SerializerEmpleados(serializers.ModelSerializer):
    
    class Meta:
        model = Empleados
        fields = '__all__'
