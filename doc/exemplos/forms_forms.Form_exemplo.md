# Exemplos de Classe de Formulário do Django - Herdando de forms.Form    
    Você pode usar esse formulário em suas views da mesma maneira que usaria um ModelForm, mas terá que lidar manualmente com a validação e o salvamento dos dados no caso de formulários não vinculados a modelos.

## Exemplo 1 - Criando a classe ExemploForm e validando o campo texto_curto

from django import forms

class ExemploForm(forms.Form):
    texto_curto = forms.CharField(max_length=50, required=True, min_length=3)
    texto_longo = forms.CharField(widget=forms.Textarea, required=False)
    inteiro = forms.IntegerField(min_value=0, max_value=100, required=True)
    decimal = forms.DecimalField(max_digits=5, decimal_places=2, min_value=0, required=True)
    ponto_flutuante = forms.FloatField(min_value=0, required=True)
    ativo = forms.BooleanField(required=False)
    data_hora = forms.DateTimeField(required=True, input_formats=['%Y-%m-%d %H:%M:%S'])
    data = forms.DateField(required=True, input_formats=['%Y-%m-%d'])
    hora = forms.TimeField(required=True, input_formats=['%H:%M:%S'])
    opcoes = forms.ChoiceField(choices=[('A', 'Opção A'), ('B', 'Opção B')], required=True)
    arquivo = forms.FileField(required=True)

    def clean_texto_curto(self):
        texto_curto = self.cleaned_data['texto_curto']
        if len(texto_curto) < 3:
            raise forms.ValidationError("O texto curto deve ter pelo menos 3 caracteres.")
        return texto_curto

## Exemplo 2 - Utilizando a classe ExemploForm em uma view 

    from django.shortcuts import render, redirect
    from .forms import ExemploForm
    from .models import Exemplo  # Se você estiver salvando os dados em um modelo

    def minha_view(request):
        if request.method == 'POST':
            form = ExemploForm(request.POST, request.FILES)
            if form.is_valid():
                # Processar os dados do formulário
                dados_formulario = form.cleaned_data
                # Se estiver salvando os dados em um modelo
                exemplo = Exemplo(
                    texto_curto=dados_formulario['texto_curto'],
                    texto_longo=dados_formulario['texto_longo'],
                    inteiro=dados_formulario['inteiro'],
                    decimal=dados_formulario['decimal'],
                    ponto_flutuante=dados_formulario['ponto_flutuante'],
                    ativo=dados_formulario['ativo'],
                    data_hora=dados_formulario['data_hora'],
                    data=dados_formulario['data'],
                    hora=dados_formulario['hora'],
                    opcoes=dados_formulario['opcoes'],
                    arquivo=request.FILES['arquivo']  # Salvar o arquivo enviado
                )
                exemplo.save()  # Salvar o objeto Exemplo no banco de dados
                # Redirecionar para alguma página de sucesso
                return redirect('pagina_sucesso')
        else:
            form = ExemploForm()
        
        return render(request, 'template.html', {'form': form})
