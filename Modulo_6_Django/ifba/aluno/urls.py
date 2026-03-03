from django.contrib import admin
from django.urls import path, include
from .views import home,editar,cadastrar_aluno,update,deletar_aluno

urlpatterns = [
    path('', home),    
    path('aluno/', home),      
    path('cadastrar_aluno/', cadastrar_aluno, name="cadastrar_aluno"),
    path('editar/<int:id>',editar,name="editar"),
    path('update/<int:id>',update,name="update"),
    path('deletar_aluno/<int:id>',deletar_aluno,name="deletar_aluno")
]
