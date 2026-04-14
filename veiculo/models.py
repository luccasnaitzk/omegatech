from django.db import models

class Veiculo(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('em_uso', 'Em Uso'),
        ('manutencao', 'Manutenção'),
    ]

    id_veiculo = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(unique=True, max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    bateria = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)  # Porcentagem
    localizacao_atual = models.ForeignKey('localizacao.Localizacao', on_delete=models.SET_NULL, null=True, blank=True, related_name='veiculos_atuais')

    class Meta:
        db_table = 'veiculo'

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
