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
            unidade_organizacional_id = form.cleaned_data['unidade_organizacional'].pk
            modalidade_id = form.cleaned_data['modalidade'].pk

            inscricoes = Inscricao.objects.filter(unidade_organizacional__pk=unidade_organizacional_id, modalidade__pk=modalidade_id)

            return render(request, 'core/fichainscricao.html',
                          {'form': form, 'inscricoes': inscricoes,
                           'uo': unidade_organizacional_id,
                           'modalidade': modalidade_id})
    else:
        form = InscricoesRelatorioForm()
    context = {
        'form': form
    }
    return render(request, 'core/fichainscricao.html', context)


def fichaisncricao(request, uo_id, modalidade_id):

            dados_inscritos = []
            uo_nome = ""
            modalidade_nome = ""

            inscricoes = Inscricao.objects.filter(unidade_organizacional__pk=uo_id, modalidade__pk=modalidade_id)
            if inscricoes:
                for inscr in inscricoes:
                    dados_inscrito = []
                    dados_inscrito.append(str(inscr.atleta.nome))
                    dados_inscrito.append('{:%d/%m/%Y}'.format(inscr.atleta.data_nascimento))
                    dados_inscrito.append(str(inscr.atleta.rg))
                    dados_inscrito.append(str(inscr.atleta.matricula))
                    if not uo_nome:
                        uo_nome = inscr.unidade_organizacional.nome
                    if not modalidade_nome:
                        modalidade_nome = inscr.modalidade.nome

                    dados_inscritos.append(dados_inscrito)

                return inscricao_pdf(uo_nome, modalidade_nome, dados_inscritos)

