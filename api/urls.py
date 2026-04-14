from django.urls import path, include
from .views import api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path('usuarios/', include('usuario.urls')),
    path('veiculos/', include('veiculo.urls')),
    path('corridas/', include('corrida.urls')),
    path('localizacoes/', include('localizacao.urls')),
    path('manutencoes/', include('manutencao.urls')),
    path('carteiras/', include('carteira.urls')),
    path('transacoes/', include('transacao.urls')),
    path('planos/', include('plano.urls')),
    path('assinaturas/', include('assinatura.urls')),
]