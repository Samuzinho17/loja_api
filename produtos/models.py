from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produtos(models.Model):
    nome = models.CharField(max_length=200)

    preco = models.DecimalField(max_digits=10, decimal_places=2)

    descricao = models.TextField(blank=True, null=True)

    estoque = models.IntegerField()

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    promocao = models.BooleanField(default=False)

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
from django.db import models

