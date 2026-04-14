from django.urls import path
from .views import PlanoListCreateView, PlanoRetrieveUpdateDestroyView

urlpatterns = [
    path('', PlanoListCreateView.as_view(), name='plano-list'),
    path('<int:pk>/', PlanoRetrieveUpdateDestroyView.as_view(), name='plano-detail'),
]