from django.urls import path

from .views import (
    UnidadeOrganizacionalListView,
    TipoModalidadeListView,
    ModalidadeListView,
    AtletaListView,
    AtletaPorModalidadeListView,
)

urlpatterns = [
    path('core/unidadeorganizacional/', UnidadeOrganizacionalListView.as_view(), name='unidade_organizacional'),
    path('core/tipomodalidade/', TipoModalidadeListView.as_view(), name='tipo_modalidade'),
    path('core/modalidade/', ModalidadeListView.as_view(), name='modalidade'),
    path('core/atleta/', AtletaListView.as_view(), name='atleta'),
    path('core/atletapormodalidade/', AtletaPorModalidadeListView.as_view(), name='atleta_por_modalidade'),
]
