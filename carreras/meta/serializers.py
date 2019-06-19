from rest_framework import serializers
from meta.models import Cargo, Equipos, Miembros, Carreras, Vueltas

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cargo
        fields = ('id','nombre','descripcion')

class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model= Equipos
        fields = ('id','nombre','descripcion','logo')

class MiembrosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Miembros
        fields = ('id','equipo','cargo','nombre','edad','tipo_sangre','direccion','nss')

class CarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Carreras
        fields = ('id','nombre','fecha_inicio','fecha_termino', 'estatus')

class VueltasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vueltas
        fields = ('id','equipo','carrera','vuelta', 'tiempo_total', 'tiempo_vuelta')
