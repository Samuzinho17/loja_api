from django.shortcuts import render
from .models import Produtos



def lista_produtos(request):
    produtos = Produtos.objects.all()


    return render(request,'produtos/lista_produtos.html', {'produtos': produtos})