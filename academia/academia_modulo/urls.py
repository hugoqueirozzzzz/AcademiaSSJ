from django.urls import path
from .views import home, cadastrar_aluno, listar_alunos, cadastrar_treino, listar_treinos, hipertrofia, emagrecimento, condicionamento, forca, cardio

app_name = "academia_modulo"

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('listar_alunos/', listar_alunos, name='listar_alunos'),
    path('cadastrar_treino/', cadastrar_treino, name='cadastrar_treino'),
    path('listar_treinos/', listar_treinos, name='listar_treinos'),
    path('listar_treinos/hipertrofia/', hipertrofia, name='hipertrofia'),
    path('listar_treinos/emagrecimento/', emagrecimento, name='emagrecimento'),
    path('listar_treinos/condicionamento/', condicionamento, name='condicionamento'),
    path('listar_treinos/forca/', forca, name='forca'),
    path('listar_treinos/cardio/', cardio, name='cardio'),

    
]