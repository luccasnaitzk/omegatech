from rest_framework import serializers
from usuario.models import Usuario
from veiculo.models import Veiculo
from corrida.models import Corrida
from localizacao.models import Localizacao
from manutencao.models import Manutencao
from carteira.models import Carteira
from transacao.models import Transacao
from plano.models import Plano
from assinatura.models import Assinatura

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def validate_cpf(self, value):
        if value and len(value) != 14:
            raise serializers.ValidationError("CPF deve ter 14 caracteres.")
        return value

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class CorridaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corrida
        fields = '__all__'

    def validate(self, data):
        usuario = data.get('usuario')
        if usuario and not usuario.assinaturas.filter(ativa=True).exists():
            raise serializers.ValidationError("Usuário não possui assinatura ativa.")
        return data

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'

class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = '__all__'

class CarteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carteira
        fields = '__all__'

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'

class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = '__all__'

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinatura
        fields = '__all__'