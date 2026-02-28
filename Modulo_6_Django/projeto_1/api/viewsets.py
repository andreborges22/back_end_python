from rest_framework import viewsets
from aluno.models import Aluno
from .serializers import AlunoSerializer

# Create your views here.
#Implementa um crud completo de forma automatica
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

#def home(request):
    #return render(request,'curso/home.html')