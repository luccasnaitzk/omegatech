from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transacao
from .serializers import TransacaoSerializer

class TransacaoListCreateView(generics.ListCreateAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

class TransacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
