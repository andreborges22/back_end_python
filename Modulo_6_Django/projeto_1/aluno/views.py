from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Aluno, Curso
import requests


# Create your views here.
def home(request):
    alunos = Aluno.objects.all()
    cursos = Curso.objects.all()
    return render(request, 'aluno/home.html', {"alunos": alunos, "cursos": cursos})


def cadastrar_aluno(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    nascimento = request.POST.get("nascimento")
    cep = request.POST.get("cep")
    bairro = request.POST.get("bairro")
    logradouro = request.POST.get("logradouro")
    numero = request.POST.get("numero")
    cidade = request.POST.get("localidade")
    estado = request.POST.get("estado")
    #ao usar o nome 'curso_id' o django converte o valor do campo que chega como string, em um valor inteiro
    curso_id = request.POST.get("curso")

    Aluno.objects.create(
        nome=nome,
        email=email,
        nascimento=nascimento,
        cep=cep,
        bairro=bairro,
        logradouro=logradouro,
        numero=numero,
        cidade=cidade,
        estado=estado,
        curso_id=curso_id,
    )
    messages.success(request, f"Estudante {nome} cadastrado(a) com sucesso!")
    return redirect(home)


def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    cursos = Curso.objects.all()
    return render(request, "aluno/update.html", {"aluno": aluno, "cursos": cursos})


def update(request, id):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    nascimento = request.POST.get("nascimento")
    cep = request.POST.get("cep")
    bairro = request.POST.get("bairro")
    logradouro = request.POST.get("logradouro")
    numero = request.POST.get("numero")
    cidade = request.POST.get("localidade")
    estado = request.POST.get("estado")
    curso_id = request.POST.get('curso')
    aluno = Aluno.objects.get(id=id)
    aluno.nome = nome
    aluno.email = email
    aluno.nascimento = nascimento
    aluno.cep = cep
    aluno.bairro = bairro
    aluno.logradouro = logradouro
    aluno.numero = numero
    aluno.cidade = cidade
    aluno.estado = estado
    aluno.curso = Curso.objects.get(id=curso_id)
    aluno.save()
    messages.success(request, f"Estudante {nome} editado(a) com sucesso!")
    return redirect(home)


def deletar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    messages.warning(
        request, f"Estudante {aluno.nome} removido(a) com sucesso!")
    return redirect(home)
