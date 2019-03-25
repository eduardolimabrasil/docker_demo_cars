from django.shortcuts import render
from carro.models import Carro
from carro.serializers import CarroSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class CarroViews(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer