from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Aluno


def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {"alunos": alunos})


def cadastrar_aluno(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    nascimento = request.POST.get("nascimento")
    Aluno.objects.create(nome=nome, email=email, nascimento=nascimento)
    messages.success(request, "Aluno cadastrado com sucesso!")
    return redirect(home)


"""def criar_aluno(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    nascimento = request.POST.get("nascimento")
    Aluno.objects.create(nome=nome, email=email, nascimento=nascimento)
    messages.success(request, "Aluno cadastrado com sucesso!")
    return redirect(home)
"""

"""def editar_aluno(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    nascimento = request.POST.get("nascimento")
    Aluno.objects.create(nome=nome, email=email, nascimento=nascimento)
    messages.success(request, "Aluno atualizado com sucesso!")
    return redirect(home)
"""

def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, "update.html", {"aluno": aluno})


def update(request, id):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    nascimento = request.POST.get("nascimento")
    aluno = Aluno.objects.get(id=id)
    aluno.nome = nome
    aluno.email = email
    aluno.nascimento = nascimento
    aluno.save()
    messages.success(request, "Aluno editado com sucesso!")
    return redirect(home)


def deletar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    messages.warning(request, "Aluno removido com sucesso!")
    return redirect(home)
