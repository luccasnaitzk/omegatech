from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Manutencao
from .serializers import ManutencaoSerializer

class ManutencaoListCreateView(generics.ListCreateAPIView):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer

class ManutencaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer
