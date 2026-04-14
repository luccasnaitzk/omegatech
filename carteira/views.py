from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Carteira
from .serializers import CarteiraSerializer
from transacao.models import Transacao

class CarteiraListCreateView(generics.ListCreateAPIView):
    queryset = Carteira.objects.all()
    serializer_class = CarteiraSerializer

class CarteiraRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carteira.objects.all()
    serializer_class = CarteiraSerializer

@api_view(['POST'])
def carteira_adicionar_saldo(request, pk):
    carteira = get_object_or_404(Carteira, pk=pk)
    valor = request.data.get('valor')
    if not valor:
        return Response({"detail": "Valor é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
    Transacao.objects.create(
        carteira=carteira,
        tipo='credito',
        valor=valor,
        descricao="Adição de saldo"
    )
    return Response({"detail": "Saldo adicionado."})
