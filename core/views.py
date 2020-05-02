from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
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

from .forms import (
    RelatorioInscricoesForm,
    RelatorioAtletasCampusForm,
    RelatorioAtletasModalidadeForm,
    RelatorioAtletasTipoModalidadeForm,
)

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
def logoutList(request):
    return redirect('/accounts/logout/')


@login_required
def unidadeOrganizacionalList(request):
    search = request.GET.get('search')
    unidadades_organizacionais = None

    if search:
        unidadades_organizacionais_list = UnidadeOrganizacional.objects.filter(nome__icontains=search).order_by('nome')
    else:
        unidadades_organizacionais_list = UnidadeOrganizacional.objects.all().order_by('nome')

    if unidadades_organizacionais_list:

        paginator = Paginator(unidadades_organizacionais_list, 10)

        page = request.GET.get('page')
        unidadades_organizacionais = paginator.get_page(page)

    else:
        messages.info(request, 'Nenhuma Unidade Organizacional localizada!')

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


class UnidadeOrganizacionalUpdateView(UpdateView):
    model = UnidadeOrganizacional
    fields = ["nome"]
    context_object_name = 'unidade_organizacional'
    success_url = "/unidadeorganizacional"


class UnidadeOrganizacionalDeleteView(DeleteView):
    model = UnidadeOrganizacional
    context_object_name = 'unidade_organizacional'
    success_url = "/unidadeorganizacional"


@login_required
def inscricoesList(request):
    form = RelatorioInscricoesForm(request.POST or None)

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
        form = RelatorioInscricoesForm()
    context = {
        'form': form
    }
    return render(request, 'core/fichainscricao.html', context)


@login_required
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


@login_required
def atletaCampusList(request):
    form = RelatorioAtletasCampusForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['unidade_organizacional']:
                unidade_organizacional_id = form.cleaned_data['unidade_organizacional'].pk
                inscricoes = Inscricao.objects.filter(unidade_organizacional__pk=unidade_organizacional_id).order_by('atleta__nome')
                mostrar_campus = False
            else:
                inscricoes = Inscricao.objects.all().order_by('unidade_organizacional__nome', 'atleta__nome')
                mostrar_campus = True

            return render(request, 'core/atletacampus.html',
                          {'form': form, 'inscricoes': inscricoes, 'mostrar_campus': mostrar_campus})
    else:
        form = RelatorioAtletasCampusForm()
    context = {
        'form': form
    }
    return render(request, 'core/atletacampus.html', context)


@login_required
def atletaModalidadeList(request):
    form = RelatorioAtletasModalidadeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['modalidade']:
                modalidade_id = form.cleaned_data['modalidade'].pk
                inscricoes = Inscricao.objects.filter(modalidade__pk=modalidade_id).order_by('atleta__nome')
                mostrar_modalidade = False
            else:
                inscricoes = Inscricao.objects.all().order_by('modalidade__nome', 'atleta__nome')
                mostrar_modalidade = True

            return render(request, 'core/atletamodalidade.html',
                          {'form': form, 'inscricoes': inscricoes, 'mostrar_modalidade': mostrar_modalidade})
    else:
        form = RelatorioAtletasModalidadeForm()
    context = {
        'form': form
    }
    return render(request, 'core/atletamodalidade.html', context)


@login_required
def atletaTipoModalidadeList(request):
    form = RelatorioAtletasTipoModalidadeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['tipo_modalidade']:
                tipo_modalidade_id = form.cleaned_data['tipo_modalidade'].pk
                inscricoes = Inscricao.objects.filter(modalidade__tipo_modalidade__pk=tipo_modalidade_id).order_by('atleta__nome')
                mostrar_tipo_modalidade = False
            else:
                inscricoes = Inscricao.objects.all().order_by('modalidade__tipo_modalidade__nome', 'atleta__nome')
                mostrar_tipo_modalidade = True

            return render(request, 'core/atletatipomodalidade.html',
                          {'form': form, 'inscricoes': inscricoes, 'mostrar_tipo_modalidade': mostrar_tipo_modalidade})
    else:
        form = RelatorioAtletasTipoModalidadeForm()
    context = {
        'form': form
    }
    return render(request, 'core/atletatipomodalidade.html', context)
