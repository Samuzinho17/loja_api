from django.contrib import admin
from .models import Categoria, Produtos
from django.utils.html import format_html

admin.site.register(Produtos)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'categoria',
        'preco',
        'estoque',
        'promocao',
        'imagem_preview',
        'data_criacao'
    )

    list_filter = ('categoria', 'promocao')

    search_fields = ('nome', 'descricao')