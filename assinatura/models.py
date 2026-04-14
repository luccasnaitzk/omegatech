from django.db import models
from django.utils import timezone

class Assinatura(models.Model):
    id_assinatura = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='assinaturas')
    plano = models.ForeignKey('plano.Plano', on_delete=models.CASCADE, related_name='assinaturas')
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField()
    ativa = models.BooleanField(default=True)

    class Meta:
        db_table = 'assinatura'
        app_label = 'assinatura'

    def __str__(self):
        return f"Assinatura {self.id_assinatura} - {self.usuario.nome}"

    def save(self, *args, **kwargs):
        if not self.data_fim:
            self.data_fim = self.data_inicio + timezone.timedelta(days=self.plano.duracao_dias)
        super().save(*args, **kwargs)
