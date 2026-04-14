from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Assinatura
from .serializers import AssinaturaSerializer

class AssinaturaListCreateView(generics.ListCreateAPIView):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer

class AssinaturaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer
