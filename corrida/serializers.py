from rest_framework import serializers
from .models import Corrida

class CorridaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corrida
        fields = '__all__'

    def validate(self, data):
        usuario = data.get('usuario')
        if usuario and not usuario.assinaturas.filter(ativa=True).exists():
            raise serializers.ValidationError("Usuário não possui assinatura ativa.")
        return data