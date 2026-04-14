from django.urls import path
from .views import CarteiraListCreateView, CarteiraRetrieveUpdateDestroyView, carteira_adicionar_saldo

urlpatterns = [
    path('', CarteiraListCreateView.as_view(), name='carteira-list'),
    path('<int:pk>/', CarteiraRetrieveUpdateDestroyView.as_view(), name='carteira-detail'),
    path('<int:pk>/adicionar-saldo/', carteira_adicionar_saldo, name='carteira-adicionar-saldo'),
]