from django.db import models

# Create your models here.
class Carro(models.Model):
    name = models.CharField(max_length=30)
    ano = models.IntegerField()
    marca = models.CharField(max_length=15)
    tipo = models.CharField(max_length=10)
    preco = models.FloatField()
