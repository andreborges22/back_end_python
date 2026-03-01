from rest_framework import viewsets
from aluno.models import Aluno
from curso.models import Curso
from .serializers import AlunoSerializer, CursoSerializer

# Create your views here.
# Implementa um crud completo para os alunos de forma automatica
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

# Implementa um crud completo para os cursos de forma automatica
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
