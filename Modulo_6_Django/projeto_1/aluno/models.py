from django.db import models

# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    nascimento = models.DateField(null=True)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100, default="")
    logradouro = models.CharField(max_length=100, default="")
    numero = models.CharField(max_length=10, default="")
    cidade = models.CharField(max_length=100, default="")
    estado = models.CharField(max_length=2, default="")    

    def __str__(self):
        return self.nome
