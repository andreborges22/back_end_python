from rest_framework import serializers
from .models import Curso

#cria campos com base no modelo
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        #retorna todos os campos do banco
        fields = "__all__"
        #se quiser apenas alguns campos especificos, faz dessa forma:
        # fields = ["id","nome"]