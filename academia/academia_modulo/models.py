from django.db import models
from datetime import date

# Create your models here.

class Aluno (models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    plano = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    nascimento = models.DateField()
    pagamento = models.TextChoices('Pagamento', ['DINHEIRO', 'CARTAO', 'PIX']) 
    frequencia = models.CharField(max_length=3)
    status = models.BooleanField(default=True)

class Ficha (models.Model):
    exercicios = models.CharField(max_length=100)
    series = models.IntegerField()
    repeticoes = models.CharField(max_length=10)
    tipo = models.CharField(max_length=100)


class Treino (models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    idade = models.IntegerField()
    imc = models.IntegerField()
    ficha_de_treino = models.ForeignKey(Ficha, on_delete=models.CASCADE)

