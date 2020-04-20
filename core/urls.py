from django.urls import path

from .views import UnidadeOrganizacionalListView, TipoModalidadeListView

urlpatterns = [
    path('core/unidadeorganizacional/', UnidadeOrganizacionalListView.as_view(), name='unidade_organizacional'),
    path('core/tipomodalidade/', TipoModalidadeListView.as_view(), name='tipo_modalidade'),
]
