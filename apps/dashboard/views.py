from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator


from visitantes.models import Visitante

from django.utils import timezone
# from datetime import datetime


@login_required
def index(request):

    # todos_visitantes = Visitante.objects.all()

    #  --> ordenado por horario_chegada --> ordem descendente devido o sinal (-)
    todos_visitantes = Visitante.objects.order_by("-horario_chegada")

    # --> procedimento para popular as informaçoes na dashboard
    # filtro executado pelo status do visita
    visitantes_aguardando = todos_visitantes.filter(status="AGUARDANDO")
    visitantes_em_visita = todos_visitantes.filter(status="EM_VISITA")
    visitantes_finalizado = todos_visitantes.filter(status="FINALIZADO")

    hora_atual = timezone.now()
    mes_atual = hora_atual.month

    # filtro executado pelo data da visita, neste caso todos os visitante com esta data
    # usando criterio de busca --> lookup
    # visitantes_date = todos_visitantes.filter(horario_chegada__date = "2021-07-17"

    # usando criterio de busca --> lookup -> buscando pelo mes
    visitantes_mes = todos_visitantes.filter(horario_chegada__month=mes_atual)

    # --> procedimento para alterar o printout de saida sendo a data
    #  alterar o filtro de busca Visitante.objects.all() --> Visitante.objects.order_by

    # paginando resultados para exibir de 10 em 10 itens
    # numero_pagina = request.GET.get('page', 1)
    # visitantes_paginados = Paginator(visitantes, 10)
    # pagina_obj = visitantes_paginados.get_page(numero_pagina)

    context = {
        "nome_pagina": "Início da Dashbord",
        "todos_visitantes": todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizado": visitantes_finalizado.count(),
        "visitantes_mes": visitantes_mes.count(),
        # "pagina_obj": pagina_obj
    }
    return render(request, 'index.html', context)
