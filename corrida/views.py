from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Corrida
from .serializers import CorridaSerializer
from transacao.models import Transacao

class CorridaListCreateView(generics.ListCreateAPIView):
    queryset = Corrida.objects.all()
    serializer_class = CorridaSerializer

class CorridaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Corrida.objects.all()
    serializer_class = CorridaSerializer

@api_view(['POST'])
def corrida_iniciar(request, pk):
    corrida = get_object_or_404(Corrida, pk=pk)
    if corrida.status != 'ativa':
        return Response({"detail": "Corrida já iniciada ou finalizada."}, status=status.HTTP_400_BAD_REQUEST)
    corrida.veiculo.status = 'em_uso'
    corrida.veiculo.save()
    return Response({"detail": "Corrida iniciada."})

@api_view(['POST'])
def corrida_finalizar(request, pk):
    corrida = get_object_or_404(Corrida, pk=pk)
    if corrida.status != 'ativa':
        return Response({"detail": "Corrida não está ativa."}, status=status.HTTP_400_BAD_REQUEST)
    corrida.status = 'finalizada'
    corrida.data_fim = timezone.now()
    corrida.save()
    corrida.veiculo.status = 'disponivel'
    corrida.veiculo.save()
    Transacao.objects.create(
        carteira=corrida.usuario.carteira,
        tipo='debito',
        valor=corrida.custo or 0,
        descricao=f"Pagamento da corrida {corrida.id_corrida}"
    )
    return Response({"detail": "Corrida finalizada e pagamento registrado."})
