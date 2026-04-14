from rest_framework import serializers
from .models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'
        extra_kwargs = {
            'modelo': {
                'help_text': 'Modelo do veículo.',
            },
            'placa': {
                'help_text': 'Placa única do veículo.',
            },
            'status': {
                'help_text': 'Status atual do veículo: disponivel, em_uso ou manutencao.',
            },
            'bateria': {
                'help_text': 'Nível de bateria em porcentagem.',
            },
            'localizacao_atual': {
                'help_text': 'ID da localização atual do veículo (opcional).',
                'required': False,
            },
        }