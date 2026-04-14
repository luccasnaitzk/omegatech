from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Localizacao
from .serializers import LocalizacaoSerializer

class LocalizacaoListCreateView(generics.ListCreateAPIView):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer

class LocalizacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
