from django.urls import path
from .views import (
    UsuarioListCreateView,
    UsuarioRetrieveUpdateDestroyView,
    usuario_carteira,
    usuario_assinatura_ativa,
)

urlpatterns = [
    path('', UsuarioListCreateView.as_view(), name='usuario-list'),
    path('<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
    path('<int:pk>/carteira/', usuario_carteira, name='usuario-carteira'),
    path('<int:pk>/assinatura-ativa/', usuario_assinatura_ativa, name='usuario-assinatura-ativa'),
]