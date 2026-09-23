from django.urls import path
from .views import home, cadastrar_aluno, listar_alunos, cadastrar_treino, listar_treinos, hipertrofia, emagrecimento, condicionamento, forca, cardio, aluno_edit, aluno_delete, treino_edit, treino_delete


app_name = "academia_modulo"

urlpatterns = [
    path('', home, name='home'),
    path('aluno/cadastrar/', cadastrar_aluno, name='cadastrar_aluno'),
    path('aluno/listar/', listar_alunos, name='listar_alunos'),
    path('aluno/editar/<int:pk>/', aluno_edit, name='aluno_edit'),
    path('aluno/excluir/<int:pk>/', aluno_delete, name='aluno_delete'),
    path('treino/cadastrar/', cadastrar_treino, name='cadastrar_treino'),
    path('treino/listar/', listar_treinos, name='listar_treinos'),
    path('treino/editar/<int:treino_id>/', treino_edit, name='treino_edit'),
    path('treino/excluir/<int:treino_id>/', treino_delete, name='treino_delete'),
    path('listar_treinos/hipertrofia/', hipertrofia, name='hipertrofia'),
    path('listar_treinos/emagrecimento/', emagrecimento, name='emagrecimento'),
    path('listar_treinos/condicionamento/', condicionamento, name='condicionamento'),
    path('listar_treinos/forca/', forca, name='forca'),
    path('listar_treinos/cardio/', cardio, name='cardio'),

    
]