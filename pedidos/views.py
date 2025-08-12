
from django.http import HttpResponse

def lista_pedidos(request):
    return HttpResponse("""Lista de Pedidos:<br>
    5 Bananas para Isabela<br>
    4 Milhos para Nicolle<br>
    2 Morangos para Samuel<br>
    9 Uvas para Mateus<br>
    8 Jabuticabas para Pedro Gabriel""")