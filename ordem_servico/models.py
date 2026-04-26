from django.db import models
from django.contrib.auth.models import User

# Modelo 1: Setor (Ex: Bloco A, Financeiro, Coordenação)
class Setor(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Setores" # Corrige de "Setors" para "Setores"

    def __str__(self):
        return self.nome

# Modelo 2: Categoria (Ex: TI, Infraestrutura, Limpeza)
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorias" # Corrige de "Categorias" (inglês) para "Categorias" (PT-BR)

    def __str__(self):
        return self.nome

# Modelo 3: Solicitação (O "Ticket" inicial)
class Solicitacao(models.Model):
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes')
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT) # Relacionamento ForeignKey 
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descricao = models.TextField(verbose_name="Descrição do Problema")
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Solicitação"
        verbose_name_plural = "Solicitações"

    def __str__(self):
        # Unindo Setor, Categoria e um resumo da Descrição
        return f"Setor: {self.setor} | Categoria: {self.categoria} | Descrição: {self.descricao[:40]}..."

# No Modelo 4: Perfil do Funcionário
class PerfilFuncionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Perfil de Funcionário"
        verbose_name_plural = "Perfis de Funcionários"

    def __str__(self):
        # Isso fará aparecer: "aldo [TI]" na lista de seleção da OS
        cat_nome = self.categoria.nome if self.categoria else "Geral"
        return f"{self.user.username} [{cat_nome}]"

# Modelo 5: Ordem de Serviço (O atendimento técnico)
class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    ]
    
    # Relacionamento OneToOne (Uma OS para cada Solicitação) 
    solicitacao = models.OneToOneField(Solicitacao, on_delete=models.CASCADE)
    tecnico = models.ForeignKey('PerfilFuncionario', on_delete=models.SET_NULL, null=True, related_name='atendimentos')
    diagnostico = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_abertura = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"

    def __str__(self):
        return f"OS {self.id} (Ref: {self.solicitacao.id})"
    