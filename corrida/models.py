from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Corrida(models.Model):
    STATUS_CHOICES = [
        ('ativa', 'Ativa'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
    ]

    id_corrida = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='corridas')
    veiculo = models.ForeignKey('veiculo.Veiculo', on_delete=models.CASCADE, related_name='corridas')
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(null=True, blank=True)
    localizacao_inicio = models.ForeignKey('localizacao.Localizacao', on_delete=models.CASCADE, related_name='corridas_inicio')
    localizacao_fim = models.ForeignKey('localizacao.Localizacao', on_delete=models.SET_NULL, null=True, blank=True, related_name='corridas_fim')
    distancia = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # em km
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativa')

    class Meta:
        db_table = 'corrida'
        app_label = 'corrida'

    def __str__(self):
        return f"Corrida {self.id_corrida} - {self.usuario.nome}"

    def clean(self):
        if not self.usuario.assinaturas.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now()).exists():
            raise ValidationError("Usuário não possui assinatura ativa.")
