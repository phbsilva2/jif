from django.views.generic import ListView

from .models import UnidadeOrganizacional, TipoModalidade


class UnidadeOrganizacionalListView(ListView):
    template_name = 'unidade_organizacional.html'
    model = UnidadeOrganizacional
    paginate_by = 2
    ordering = 'nome'


class TipoModalidadeListView(ListView):
    model = TipoModalidade
