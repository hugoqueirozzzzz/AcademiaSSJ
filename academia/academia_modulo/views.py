from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastrar_aluno(request):
    return render(request, 'cadastrar_aluno.html')

def listar_alunos(request):
    return render(request, 'listar_alunos.html')

def cadastrar_treino(request):
    return render(request, 'cadastrar_treino.html')

def listar_treinos(request):
    return render(request, 'listar_treinos.html')

def hipertrofia (request):
    return render(request, 'hipertrofia.html')

def emagrecimento (request):
    return render(request, 'emagrecimento.html')

def condicionamento (request):
    return render(request, 'condicionamento.html')

def forca (request):
    return render(request, 'forca.html')

def cardio (request):
    return render(request, 'cardio.html')
