from django.urls import path

from .views import UnidadeOrganizacionalListView

urlpatterns = [
    path('core/unidadeorganizacional/', UnidadeOrganizacionalListView.as_view(), name='unidade_organizacional'),
]