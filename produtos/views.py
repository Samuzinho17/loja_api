
from django.http import HttpResponse

def lista_produtos(request):
    return HttpResponse("""Lista de Produtos:<br>
    Banana<br>
    Milho<br>
    Morango<br>
    Uva<br>
    Jabuticaba""")