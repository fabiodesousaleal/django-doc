from django import forms
class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'w-full text-base px-4 py-4 border-b border-gray-300 focus:outline-none rounded-full text-center font-semibold focus:border-indigo-500',
                'placeholder': 'login',
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'w-full text-base px-4 py-4 border-b border-gray-300 focus:outline-none rounded-full text-center font-semibold focus:border-indigo-500',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )