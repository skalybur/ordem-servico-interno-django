from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Solicitacao, OrdemServico

# 1. Listagem (Read)
class SolicitacaoListView(LoginRequiredMixin, ListView):
    model = Solicitacao
    template_name = 'ordem_servico/solicitacao_list.html'
    context_object_name = 'solicitacoes'
    paginate_by = 5
    ordering = ['-data_criacao']

# 2. Cadastro (Create)
class SolicitacaoCreateView(LoginRequiredMixin, CreateView):
    model = Solicitacao
    template_name = 'ordem_servico/solicitacao_form.html'
    fields = ['setor', 'categoria', 'descricao']
    success_url = reverse_lazy('solicitacao_list')

    def form_valid(self, form):
        # Vincula automaticamente o solicitante ao usuário logado
        form.instance.solicitante = self.request.user
        return super().form_valid(form)

# 3. Edição (Update)
class SolicitacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Solicitacao
    template_name = 'ordem_servico/solicitacao_form.html'
    fields = ['setor', 'categoria', 'descricao']
    success_url = reverse_lazy('solicitacao_list')

# 4. Exclusão (Delete)
class SolicitacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Solicitacao
    template_name = 'ordem_servico/solicitacao_confirm_delete.html'
    success_url = reverse_lazy('solicitacao_list')

# 5. Listagem de Ordens de Serviço (Read)
class OrdemServicoListView(LoginRequiredMixin, ListView):
    model = OrdemServico
    template_name = 'ordem_servico/ordem_servico_list.html'
    context_object_name = 'ordens'
    ordering = ['-data_abertura']

# 6. Cadastro de Ordem de Serviço (Create)
class OrdemServicoCreateView(LoginRequiredMixin, CreateView):
    model = OrdemServico
    template_name = 'ordem_servico/ordem_servico_form.html'
    fields = ['solicitacao', 'tecnico', 'diagnostico', 'status']
    success_url = reverse_lazy('os_list')

# 7. Edição de Ordem de Serviço (Update)
class OrdemServicoUpdateView(LoginRequiredMixin, UpdateView):
    model = OrdemServico
    template_name = 'ordem_servico/ordem_servico_form.html' # Reutiliza o mesmo form
    fields = ['tecnico', 'diagnostico', 'status'] # Não deixamos editar a solicitação original
    success_url = reverse_lazy('os_list')