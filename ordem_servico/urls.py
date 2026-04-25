from django.urls import path
from .views import (
    SolicitacaoListView, 
    SolicitacaoCreateView, 
    SolicitacaoUpdateView, 
    SolicitacaoDeleteView,
    OrdemServicoListView,
    OrdemServicoCreateView,
    OrdemServicoUpdateView
)

urlpatterns = [
    path('', SolicitacaoListView.as_view(), name='solicitacao_list'),
    path('nova/', SolicitacaoCreateView.as_view(), name='solicitacao_create'),
    path('editar/<int:pk>/', SolicitacaoUpdateView.as_view(), name='solicitacao_edit'),
    path('excluir/<int:pk>/', SolicitacaoDeleteView.as_view(), name='solicitacao_delete'),
    path('ordens/', OrdemServicoListView.as_view(), name='os_list'),
    path('ordens/nova/', OrdemServicoCreateView.as_view(), name='os_create'),
    path('ordens/editar/<int:pk>/', OrdemServicoUpdateView.as_view(), name='os_edit'),
]