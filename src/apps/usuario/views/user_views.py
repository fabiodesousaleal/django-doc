from django.shortcuts import render, redirect, get_object_or_404
from apps.usuario.forms import CadastroForms, LoginForms

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def index(request):
    return render(request, 'tailwind_teste.html')


def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome_login = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome_login,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                return render(request, 'home.html')
            else:
                messages.error(request, 'Usuário ou Senha inválida.')
                return redirect('login')
        return render(request, 'form_login.html', {'form': form})
    return render(request, 'form_login.html', {'form': form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            first_name = form['first_name'].value()
            last_name = form['last_name'].value()
            nome_login = form['nome_login'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=nome_login).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                last_name=last_name,
                first_name=first_name,
                username=nome_login,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, f'{usuario.username.capitalize()} você foi cadastrado(a) com sucesso!')
            return redirect('login')
    
    return render(request, 'cadastro_user.html', {'form': form, })


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
