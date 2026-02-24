from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_aluno'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name="cadastrar_aluno"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('update/<int:id>', views.update, name="update"),
    path('deletar_aluno/<int:id>', views.deletar_aluno, name="deletar_aluno")
]
