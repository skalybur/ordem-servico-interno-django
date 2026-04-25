from django.contrib import admin
# Adicione o PerfilFuncionario no import abaixo:
from .models import Setor, Categoria, Solicitacao, OrdemServico, PerfilFuncionario

admin.site.register(Setor)
admin.site.register(Categoria)
admin.site.register(Solicitacao)
admin.site.register(OrdemServico)
admin.site.register(PerfilFuncionario)