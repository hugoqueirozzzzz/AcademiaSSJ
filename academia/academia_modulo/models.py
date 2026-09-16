from django.db import models

# Create your models here.

class aluno (models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    plano = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    nascimento = models.DateField()
    pagamento = models.TextChoices('Pagamento', ['DINHEIRO', 'CARTAO', 'PIX']) 

class treino (models.Model):
    aluno = models.ForeignKey(aluno, on_delete=models.CASCADE)
    idade = models.IntegerField()
    imc = models.FloatField()
    ficha_de_treino = models.CharField(max_length=100)