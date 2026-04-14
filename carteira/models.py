from django.db import models

class Carteira(models.Model):
    id_carteira = models.AutoField(primary_key=True)
    usuario = models.OneToOneField('usuario.Usuario', on_delete=models.CASCADE, related_name='carteira')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'carteira'
        app_label = 'carteira'

    def __str__(self):
        return f"Carteira de {self.usuario.nome}"
