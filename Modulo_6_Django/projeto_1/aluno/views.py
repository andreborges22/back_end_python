from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Aluno

# Create your views here.
def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/home.html',{"alunos": alunos})

def cadastrar_aluno(request):
    nome = request.POST.get("nome")
    print(request.POST)
    email = request.POST.get("email")
    print(request.POST)
    nascimento = request.POST.get("nascimento")
    print(request.POST)        
    Aluno.objects.create(nome=nome, email=email, nascimento=nascimento)
    messages.success(request, "Aluno cadastrado com sucesso!")
    return redirect(home)