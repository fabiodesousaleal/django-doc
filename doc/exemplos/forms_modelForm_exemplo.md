# Exemplos de Classe de Formulário do Django - Herdando de ModelForm

## Herdando de ModelForm

### Exemplo 1 - criando a classe ExemploForm, por convenção deve ser criada no arquivo forms.py
    from django import forms
    from .models import Exemplo  # Importe o modelo Exemplo aqui

    class ExemploForm(forms.ModelForm):
        class Meta:
            model = Exemplo  # Especifique o modelo que o formulário vai representar
            fields = '__all__'  # Ou especifique os campos que deseja incluir no formulário

### Exemplo 2 - Utilizando a classe ExemploForm em uma view

    from django.shortcuts import render
    from .forms import ExemploForm

    def minha_view(request):
        if request.method == 'POST':
            form = ExemploForm(request.POST)
            if form.is_valid():
                # Processar os dados do formulário
                form.save()
                # Redirecionar para alguma página de sucesso
        else:
            form = ExemploForm()
        
        return render(request, 'template.html', {'form': form})
