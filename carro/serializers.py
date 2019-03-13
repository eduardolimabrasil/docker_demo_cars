from rest_framework import serializers
from carro.models import Carro

class CarroSerializer(serializers.Serializer):
    class Meta():
        model = Carro
        fields = '__all__'