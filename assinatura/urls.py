from django.urls import path
from .views import AssinaturaListCreateView, AssinaturaRetrieveUpdateDestroyView

urlpatterns = [
    path('', AssinaturaListCreateView.as_view(), name='assinatura-list'),
    path('<int:pk>/', AssinaturaRetrieveUpdateDestroyView.as_view(), name='assinatura-detail'),
]