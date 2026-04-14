from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'nome': {
                'help_text': 'Nome completo do usuário.',
            },
            'cpf': {
                'help_text': 'CPF com ou sem formatação, 11 dígitos.',
            },
            'email': {
                'help_text': 'Email válido do usuário.',
            },
            'telefone': {
                'help_text': 'Telefone de contato.',
            },
            'data_nascimento': {
                'help_text': 'Data de nascimento no formato YYYY-MM-DD.',
            },
            'status': {
                'help_text': 'Status do usuário.',
            },
        }

    def validate_cpf(self, value):
        if value:
            digits = ''.join(filter(str.isdigit, value))
            if len(digits) != 11:
                raise serializers.ValidationError("CPF deve ter 11 dígitos, com ou sem formatação.")
        return value