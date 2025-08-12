from django.db import models

class Pedidos(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.nome
from django.db import models