from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name = "Lista_produtos"),
]