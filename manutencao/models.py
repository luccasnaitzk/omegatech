from django.db import models
from django.utils import timezone

class Manutencao(models.Model):
    id_manutencao = models.AutoField(primary_key=True)
    veiculo = models.ForeignKey('veiculo.Veiculo', on_delete=models.CASCADE, related_name='manutencoes')
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(null=True, blank=True)
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'manutencao'
        app_label = 'manutencao'

    def __str__(self):
        return f"Manutenção {self.id_manutencao} - {self.veiculo.placa}"
