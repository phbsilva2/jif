from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainList, name='main_list'),
    path('unidadeorganizacional/', views.unidadeOrganizacionalList, name='unidade_organizacional_list'),
    path('unidadeorganizacional/<int:id>', views.unidadeOrganizacionalView, name="unidade_organizacional_view"),
    path('unidadeorganizacional_add/', views.unidadeOrganizacionalAdd, name="unidade_organizacional_add"),
    path('unidadeorganizacional_edit/<int:id>', views.unidadeOrganizacionalEdit, name="unidade_organizacional_edit"),
    path('unidadeorganizacional_delete/<int:id>', views.unidadeOrganizacionalDelete, name="unidade_organizacional_delete"),
    path('inscricoes/', views.inscricoesList, name='inscricoes'),
    path('fichainscricao/<int:uo_id>/<int:modalidade_id>', views.fichaisncricao, name='ficha_inscricao'),
]
