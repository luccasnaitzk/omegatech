from django.db import models
from django.utils import timezone

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('credito', 'Crédito'),
        ('debito', 'Débito'),
    ]

    id_transacao = models.AutoField(primary_key=True)
    carteira = models.ForeignKey('carteira.Carteira', on_delete=models.CASCADE, related_name='transacoes')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    data = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'transacao'
        app_label = 'transacao'

    def __str__(self):
        return f"Transação {self.id_transacao} - {self.tipo}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Atualizar saldo da carteira
        if self.tipo == 'credito':
            self.carteira.saldo += self.valor
        elif self.tipo == 'debito':
            self.carteira.saldo -= self.valor
        self.carteira.save()
