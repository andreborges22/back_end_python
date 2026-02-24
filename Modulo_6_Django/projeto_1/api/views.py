from rest_framework import viewsets
from aluno.models import Aluno
from .serializers import AlunoSerializer

# Create your views here.
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer