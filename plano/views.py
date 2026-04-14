from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Plano
from .serializers import PlanoSerializer

class PlanoListCreateView(generics.ListCreateAPIView):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer

class PlanoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer
