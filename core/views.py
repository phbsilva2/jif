from django.views.generic import ListView

from .models import (
    UnidadeOrganizacional,
    TipoModalidade,
    Modalidade
)


class UnidadeOrganizacionalListView(ListView):
    model = UnidadeOrganizacional


class TipoModalidadeListView(ListView):
    model = TipoModalidade


class ModalidadeListView(ListView):
    model = Modalidade
