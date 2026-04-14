from django.urls import path
from .views import LocalizacaoListCreateView, LocalizacaoRetrieveUpdateDestroyView

urlpatterns = [
    path('', LocalizacaoListCreateView.as_view(), name='localizacao-list'),
    path('<int:pk>/', LocalizacaoRetrieveUpdateDestroyView.as_view(), name='localizacao-detail'),
]