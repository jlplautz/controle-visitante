from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

from visitantes.models import Visitante
from visitantes.forms import VisitanteForm, AutorizaVisitanteForm

from django.utils import timezone


@login_required
def registrar_visitante(request):

    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            # atribuindo a estancia do save para um variavel com parametro commit False
            # procedimento utilizado para alterar o metodo save.
            visitante = form.save(commit=False)
            visitante.registrado_por = request.user.porteiro
            visitante.save()

            messages.success(
                request, "Visitante registrado com sucesso !!!"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Registrar visitante",
        "form": form
    }
    return render(request, "registrar_visitante.html", context)


@login_required
def informacoes_visitante(request, id):

    # metodo get_object vai buscar o visitante pelo Id desejado
    visitante = get_object_or_404(Visitante, id=id)
    morador = visitante.morador_responsavel
    print(morador)

    form = AutorizaVisitanteForm()

    # procedimento para alterar o objecto visitante do ID que foi passado na função
    if request.method == "POST":
        form = AutorizaVisitanteForm(
            request.POST,
            instance=visitante
        )

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()

            visitante.save()

            messages.success(request, "Entrada de visitante alterada com sucesso")

            return redirect("index")

    context = {
        "nome_pagina": "Informações de visitante",
        "visitante": visitante,
        "form": form
    }

    return render(request, "informacoes_visitante.html", context)


@login_required
def finalizar_visita(request, id):

    if request.method == "POST":
        visitante = get_object_or_404(Visitante, id=id)

        visitante.status = "FINALIZADO"
        visitante.horario_saida = timezone.now()

        visitante.save()

        messages.success(request, "Visita finalizada com sucesso")

        return redirect('index')

    else:
        return HttpResponseNotAllowed(["POST"], "Método não permitido")
