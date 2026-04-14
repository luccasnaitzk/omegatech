from django.urls import path
from .views import TransacaoListCreateView, TransacaoRetrieveUpdateDestroyView

urlpatterns = [
    path('', TransacaoListCreateView.as_view(), name='transacao-list'),
    path('<int:pk>/', TransacaoRetrieveUpdateDestroyView.as_view(), name='transacao-detail'),
]