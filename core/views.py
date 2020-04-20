from django.views.generic import ListView

from .models import UnidadeOrganizacional, TipoModalidade


class UnidadeOrganizacionalListView(ListView):
    model = UnidadeOrganizacional


class TipoModalidadeListView(ListView):
    model = TipoModalidade
