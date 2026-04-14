from django.urls import path
from .views import VeiculoListCreateView, VeiculoRetrieveUpdateDestroyView, veiculo_disponiveis

urlpatterns = [
    path('', VeiculoListCreateView.as_view(), name='veiculo-list'),
    path('<int:pk>/', VeiculoRetrieveUpdateDestroyView.as_view(), name='veiculo-detail'),
    path('disponiveis/', veiculo_disponiveis, name='veiculo-disponiveis'),
]