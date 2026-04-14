from django.db import models

class Plano(models.Model):
    id_plano = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao_dias = models.IntegerField()  

    class Meta:
        db_table = 'plano'
        app_label = 'plano'

    def __str__(self):
        return self.nome
