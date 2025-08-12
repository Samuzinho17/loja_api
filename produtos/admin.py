from django.contrib import admin
from .models import Categoria, Produtos
from django.utils.html import format_html

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'categoria',
        'preço',
        'estoque',
        'promoçao',
        'imagem_preview',
        'data_criaçao'
    )

    list_filter = ('categoria', 'promoçao')

    search_fields = ('nome', 'descriçao')