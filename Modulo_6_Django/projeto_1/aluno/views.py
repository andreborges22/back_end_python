from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Aluno
import requests


# Create your views here.
def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/home.html', {"alunos": alunos})


def cadastrar_aluno(request):
    nome = request.POST.get("nome")
    # print(request.POST)
    email = request.POST.get("email")
    # print(request.POST)
    nascimento = request.POST.get("nascimento")
    # print(request.POST)
    Aluno.objects.create(nome=nome, email=email, nascimento=nascimento)
    messages.success(request, f"Estudante {nome} cadastrado(a) com sucesso!")
    return redirect(home)


def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, "aluno/update.html", {"aluno": aluno})


def update(request, id):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    nascimento = request.POST.get("nascimento")
    aluno = Aluno.objects.get(id=id)
    aluno.nome = nome
    aluno.email = email
    aluno.nascimento = nascimento
    aluno.save()
    messages.success(request, f"Estudante {nome} editado(a) com sucesso!")
    return redirect(home)


def deletar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    messages.warning(request, f"Estudante {aluno.nome} removido(a) com sucesso!")
    return redirect(home)
