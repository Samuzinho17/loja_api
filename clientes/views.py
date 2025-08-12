
from django.http import HttpResponse

def lista_clientes(request):
    return HttpResponse("""Lista de Clientes:<br>
    Pedro Gabriel<br>
    Nicolle<br>
    Mateus<br>
    Samuel<br>
    Isabela""")
