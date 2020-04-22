from django.views.generic import ListView

from .models import (
    UnidadeOrganizacional,
    TipoModalidade,
    Modalidade,
    Atleta,
)


class UnidadeOrganizacionalListView(ListView):
    model = UnidadeOrganizacional


class TipoModalidadeListView(ListView):
    model = TipoModalidade


class ModalidadeListView(ListView):
    model = Modalidade


class AtletaListView(ListView):
    model = Atleta
