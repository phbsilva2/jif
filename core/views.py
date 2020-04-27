from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import UnidadeOrganizacionalModelForm
from .models import (
    UnidadeOrganizacional,
    TipoModalidade,
    Modalidade,
    Atleta,
    AtletaPorModalidade,
    Inscricao,
)

from .forms import InscricoesRelatorioForm
from .reports import inscricao_pdf


class UnidadeOrganizacionalListView(ListView):
    model = UnidadeOrganizacional


class TipoModalidadeListView(ListView):
    model = TipoModalidade


class ModalidadeListView(ListView):
    model = Modalidade


class AtletaListView(ListView):
    model = Atleta


class AtletaPorModalidadeListView(ListView):
    model = AtletaPorModalidade


class InscricaoListView(ListView):
    model = Inscricao


@login_required
def mainList(request):
    return render(request, 'core/main.html')

@login_required
def unidadeOrganizacionalList(request):
    search = request.GET.get('search')

    if search:
        unidadades_organizacionais_list = UnidadeOrganizacional.objects.filter(nome__icontains=search)
    else:
        unidadades_organizacionais_list = UnidadeOrganizacional.objects.all()

    paginator = Paginator(unidadades_organizacionais_list, 10)

    page = request.GET.get('page')
    unidadades_organizacionais = paginator.get_page(page)

    return render(request, 'core/unidadeorganizacional_list.html',
                  {'unidadades_organizacionais': unidadades_organizacionais})


@login_required
def unidadeOrganizacionalView(request, id):
    unidade_organizacional = get_object_or_404(UnidadeOrganizacional, pk=id)
    return render(request, 'core/unidadeorganizacional.html',
                  {'unidade_organizacional': unidade_organizacional})


@login_required
def unidadeOrganizacionalAdd(request):
    if request.method == 'POST':
        form = UnidadeOrganizacionalModelForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/unidadeorganizacional')
    else:
        form = UnidadeOrganizacionalModelForm()
        return render(request, 'core/unidadeorganizacional_add.html', {'form': form})


@login_required
def unidadeOrganizacionalEdit(request, id):
    unidade_organizacional = get_object_or_404(UnidadeOrganizacional, pk=id)
    form = UnidadeOrganizacionalModelForm(instance=unidade_organizacional)

    if request.method == 'POST':
        form = UnidadeOrganizacionalModelForm(request.POST, instance=unidade_organizacional)

        if form.is_valid():
            unidade_organizacional.save()
            return redirect('/unidadeorganizacional')
        else:
            return render(request, 'core/unidadeorganizacional_edit.html',
                          {'form': form, 'unidade_organizacional': unidade_organizacional})
    else:
        return render(request, 'core/unidadeorganizacional_edit.html',
                      {'form': form, 'unidade_organizacional': unidade_organizacional})


@login_required
def unidadeOrganizacionalDelete(request, id):
    unidade_organizacional = get_object_or_404(UnidadeOrganizacional, pk=id)
    unidade_organizacional.delete()

    messages.info(request, 'Unidade Organizacional deletada com sucesso.')

    return redirect('/unidadeorganizacional')


def inscricoesList(request):
    form = InscricoesRelatorioForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            unidade_organizacional = form.cleaned_data['unidade_organizacional']
            modalidade = form.cleaned_data['modalidade']

            dados_inscritos = []

            inscricoes = Inscricao.objects.filter(unidade_organizacional=unidade_organizacional, modalidade=modalidade)
            if inscricoes:
                for inscr in inscricoes:
                    dados_inscrito = []
                    dados_inscrito.append(str(inscr.atleta.nome))
                    dados_inscrito.append(str(inscr.atleta.nome))
                    dados_inscrito.append(str(inscr.atleta.rg))
                    dados_inscrito.append(str(inscr.atleta.matricula))

                    dados_inscritos.append(dados_inscrito)

                return inscricao_pdf(unidade_organizacional, modalidade, dados_inscritos)

    else:
        form = InscricoesRelatorioForm()
    context = {
        'form': form
    }
    return render(request, 'core/inscricoes.html', context)
