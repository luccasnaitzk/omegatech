from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer
from carteira.serializers import CarteiraSerializer
from assinatura.serializers import AssinaturaSerializer

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        cpf = self.request.query_params.get('cpf')
        search = self.request.query_params.get('search')
        if cpf:
            queryset = queryset.filter(cpf=cpf)
        if search:
            queryset = queryset.filter(Q(nome__icontains=search) | Q(email__icontains=search))
        return queryset

class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

@api_view(['GET'])
def usuario_carteira(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    carteira = usuario.carteira
    serializer = CarteiraSerializer(carteira)
    return Response(serializer.data)

@api_view(['GET'])
def usuario_assinatura_ativa(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    assinatura = usuario.assinaturas.filter(ativa=True).first()
    if assinatura:
        serializer = AssinaturaSerializer(assinatura)
        return Response(serializer.data)
    return Response({"detail": "Nenhuma assinatura ativa."}, status=status.HTTP_404_NOT_FOUND)
