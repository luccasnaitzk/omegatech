from django.db import models
from django.utils import timezone

class Localizacao(models.Model):
    id_localizacao = models.AutoField(primary_key=True)
    veiculo = models.ForeignKey('veiculo.Veiculo', on_delete=models.CASCADE, related_name='localizacoes')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'localizacao'
        app_label = 'localizacao'

    def __str__(self):
        return f"Localização {self.id_localizacao} - {self.veiculo.placa}"
