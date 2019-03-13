from django.shortcuts import render
from carro.models import Carro
from carro.serializers import CarroSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class CarroViews(viewsets.ModelViewSet):
    queryset = Carro.objects.all().values()
    serializer_class = CarroSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset)
        return Response(serializer.data, status=status.HTTP_200_OK )