from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    nascimento = models.DateField(null=True)

    def __str__(self):
         return self.nome