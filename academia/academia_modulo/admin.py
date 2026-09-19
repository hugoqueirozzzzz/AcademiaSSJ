from django.contrib import admin

from .models import Aluno, Treino, Ficha

admin.site.register(Aluno)
admin.site.register(Treino)
admin.site.register(Ficha)

# Register your models here.
