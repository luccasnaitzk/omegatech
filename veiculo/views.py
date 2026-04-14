from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Veiculo
from .serializers import VeiculoSerializer

class VeiculoListCreateView(generics.ListCreateAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class VeiculoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

@api_view(['GET'])
def veiculo_disponiveis(request):
    veiculos = Veiculo.objects.filter(status='disponivel')
    serializer = VeiculoSerializer(veiculos, many=True)
    return Response(serializer.data)
