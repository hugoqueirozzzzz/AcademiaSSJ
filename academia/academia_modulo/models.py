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
    forma_pagamento = models.CharField(max_length=100, default='')
   

    def __str__(self):
        return self.nome + ' - ' + self.cpf


class Ficha (models.Model):
    tipo = models.CharField(max_length=100)
  
    def __str__(self):
        return self.tipo


class Treino (models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    idade = models.IntegerField()
    altura = models.IntegerField()
    peso = models.FloatField()
    imc = models.FloatField()
    ficha_de_treino = models.ForeignKey(Ficha, on_delete=models.CASCADE)

    def __str__(self):
        return self.aluno.nome + ' - ' + self.ficha_de_treino.tipo
