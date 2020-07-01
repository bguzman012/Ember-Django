# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets  

from estudiantes import models
 
from estudiantes import serializers

class EstudianteViewSet(viewsets.ModelViewSet):  
    queryset = models.Estudiante.objects.all()
    serializer_class = serializers.EstudianteSerializer

class RepresentanteViewSet(viewsets.ModelViewSet):  
    queryset = models.Representante.objects.all()
    serializer_class = serializers.RepresentanteSerializer
# Create your views here.
