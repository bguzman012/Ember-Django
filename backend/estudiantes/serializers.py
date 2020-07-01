from rest_framework import serializers  
from estudiantes import models

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Estudiante
        fields = "__all__"

class RepresentanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Representante
        fields = "__all__"
