from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=14, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nome or f"Usuario {self.id_usuario}"
