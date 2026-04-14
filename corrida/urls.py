from django.urls import path
from .views import CorridaListCreateView, CorridaRetrieveUpdateDestroyView, corrida_iniciar, corrida_finalizar

urlpatterns = [
    path('', CorridaListCreateView.as_view(), name='corrida-list'),
    path('<int:pk>/', CorridaRetrieveUpdateDestroyView.as_view(), name='corrida-detail'),
    path('<int:pk>/iniciar/', corrida_iniciar, name='corrida-iniciar'),
    path('<int:pk>/finalizar/', corrida_finalizar, name='corrida-finalizar'),
]