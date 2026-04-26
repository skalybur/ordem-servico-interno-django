from django import forms
from .models import OrdemServico, Solicitacao

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['solicitacao', 'tecnico', 'diagnostico', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filtro de Queryset que já tínhamos
        if not self.instance.pk:
            qs = Solicitacao.objects.filter(ordemservico__isnull=True).order_by('-data_criacao')
        else:
            qs_disponiveis = Solicitacao.objects.filter(ordemservico__isnull=True)
            qs_atual = Solicitacao.objects.filter(pk=self.instance.solicitacao.pk)
            qs = (qs_disponiveis | qs_atual).distinct().order_by('-data_criacao')
        
        self.fields['solicitacao'].queryset = qs

        # MÁGICA: Criando as opções com o atributo 'data-descricao'
        # Isso permite que o JavaScript leia o texto completo depois
        choices = [('', '---------')]
        for obj in qs:
            # O terceiro elemento da tupla são os atributos da tag <option>
            choices.append((obj.pk, str(obj))) 
            
        self.fields['solicitacao'].choices = choices

    # Sobrescrevemos como o campo é renderizado para injetar o Data Attribute
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            # Busca a descrição completa no banco para essa opção específica
            obj = Solicitacao.objects.get(pk=value)
            option['attrs']['data-descricao'] = obj.descricao
        return option