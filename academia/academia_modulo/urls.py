from django.urls import path
from .views import home, cadastrar_aluno, listar_alunos, cadastrar_treino, listar_treinos

app_name = "academia_modulo"

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('listar_alunos/', listar_alunos, name='listar_alunos'),
    path('cadastrar_treino/', cadastrar_treino, name='cadastrar_treino'),
    path('listar_treinos/', listar_treinos, name='listar_treinos'),
    
    
]