from django.urls import path

from . import views

from .views import (
    UnidadeOrganizacionalCreateView,
    UnidadeOrganizacionalUpdateView,
    UnidadeOrganizacionalDeleteView,
)

urlpatterns = [
    path('', views.mainList, name='main_list'),
    path('unidadeorganizacional/', views.unidadeOrganizacionalList, name='unidade_organizacional_list'),
    path('unidadeorganizacional/<int:id>', views.unidadeOrganizacionalView, name="unidade_organizacional_view"),
    path('unidadeorganizacional_create/', UnidadeOrganizacionalCreateView.as_view()),
    path('unidadeorganizacional/<pk>/update', UnidadeOrganizacionalUpdateView.as_view()),
    path('unidadeorganizacional/<pk>/delete/', UnidadeOrganizacionalDeleteView.as_view()),
    path('inscricoes/', views.inscricoesList, name='inscricoes'),
    path('fichainscricao/<int:uo_id>/<int:modalidade_id>', views.fichaisncricao, name='ficha_inscricao'),
    path('atletacampus/', views.atletaCampusList, name='atleta_campus'),
    path('atletamodalidade/', views.atletaModalidadeList, name='atleta_modalidade'),
    path('atletatipomodalidade/', views.atletaTipoModalidadeList, name='atleta_tipo_modalidade'),
    path('logout/', views.logoutList, name='log_out'),
]
