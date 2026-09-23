from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Treino, Ficha
# Create your views here.

def home(request):
    return render(request, 'home.html')

#cadastrar alunos ok
def cadastrar_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        plano = request.POST.get('plano')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        email = request.POST.get('email')
        nascimento = request.POST.get('nascimento')
        forma_pagamento = request.POST.get('forma_pagamento')

        aluno = Aluno(
            nome=nome,
            cpf=cpf,
            plano=plano,
            telefone=telefone,
            endereco=endereco,
            email=email,
            nascimento=nascimento,
            forma_pagamento=forma_pagamento,
        )
        aluno.save()
        
        return redirect('academia_modulo:listar_alunos')


    return render(request, 'cadastrar_aluno.html')

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})

def cadastrar_treino(request):
    alunos = Aluno.objects.all()
    fichas = Ficha.objects.all()

    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        idade = request.POST.get('idade')
        altura = request.POST.get('altura')
        peso = request.POST.get('peso')
        imc = request.POST.get('imc')
        ficha_id = request.POST.get('ficha_de_treino')

        aluno = get_object_or_404(Aluno, id=aluno_id)
        ficha_de_treino = get_object_or_404(Ficha, id=ficha_id)

        treino = Treino(
            aluno=aluno,
            idade=idade,
            altura=altura,
            peso=peso,
            imc=imc,
            ficha_de_treino=ficha_de_treino
        )
        treino.save()

        return redirect('academia_modulo:listar_treinos')
    return render(request, 'cadastrar_treino.html', {'alunos': alunos, 'fichas': fichas})

def listar_treinos(request):
    treinos = Treino.objects.all()
    return render(request, 'listar_treinos.html', {'treinos': treinos}) 

def treino_edit(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    alunos = Aluno.objects.all()
    fichas = Ficha.objects.all()

    if request.method == 'POST':
        treino.aluno_id = request.POST.get('aluno')
        treino.idade = request.POST.get('idade')
        treino.altura = request.POST.get('altura')
        treino.peso = request.POST.get('peso')
        treino.imc = request.POST.get('imc')
        treino.ficha_de_treino_id = request.POST.get('ficha_de_treino')

        treino.save()
        return redirect('academia_modulo:listar_treinos')

    return render(request, 'cadastrar_treino.html', {'treino': treino, 'alunos': alunos, 'fichas': fichas})

def treino_delete(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    treino.delete()
    return redirect('academia_modulo:listar_treinos')

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

def aluno_edit(request, pk):
    aluno = get_object_or_404(Aluno, id=pk)

    if request.method == 'POST':
        aluno.nome = request.POST.get('nome')
        aluno.cpf = request.POST.get('cpf')
        aluno.plano = request.POST.get('plano')
        aluno.telefone = request.POST.get('telefone')
        aluno.endereco = request.POST.get('endereco')
        aluno.email = request.POST.get('email')
        aluno.nascimento = request.POST.get('nascimento')
        aluno.forma_pagamento = request.POST.get('forma_pagamento')

        aluno.save()
        return redirect('academia_modulo:listar_alunos')

    return render(request, 'cadastrar_aluno.html', {'aluno': aluno})




def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, id=pk)
    aluno.delete()
    return redirect('academia_modulo:listar_alunos')





    