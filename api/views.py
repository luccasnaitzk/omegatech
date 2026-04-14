from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'usuarios': reverse('usuario-list', request=request, format=format),
        'veiculos': reverse('veiculo-list', request=request, format=format),
        'corridas': reverse('corrida-list', request=request, format=format),
        'localizacoes': reverse('localizacao-list', request=request, format=format),
        'manutencoes': reverse('manutencao-list', request=request, format=format),
        'carteiras': reverse('carteira-list', request=request, format=format),
        'transacoes': reverse('transacao-list', request=request, format=format),
        'planos': reverse('plano-list', request=request, format=format),
        'assinaturas': reverse('assinatura-list', request=request, format=format),
    })