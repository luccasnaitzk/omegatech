from django.urls import path
from .views import ManutencaoListCreateView, ManutencaoRetrieveUpdateDestroyView

urlpatterns = [
    path('', ManutencaoListCreateView.as_view(), name='manutencao-list'),
    path('<int:pk>/', ManutencaoRetrieveUpdateDestroyView.as_view(), name='manutencao-detail'),
]