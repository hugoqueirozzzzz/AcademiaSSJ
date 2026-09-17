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
    
class Treino (models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    idade = models.IntegerField(max_length=3)
    imc = models.IntegerField(max_length=3)
    ficha_de_treino = models.CharField(max_length=100)
