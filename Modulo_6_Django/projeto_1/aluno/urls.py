from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_aluno'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name="cadastrar_aluno"),
]
