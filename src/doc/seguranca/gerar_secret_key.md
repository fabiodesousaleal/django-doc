# Gerar uma chave secreta aleatória
## Local de armazenamento da chave secreta do django:
    A chave de segurança do django é definida pela variavel SECRET_KEY no settings.py:
    SECRET_KEY = 'çalsdkjçlaskdlçlasd-=asdçlkjasçldçlasçljk'
 

## Criando uma nova chave aleatória utilizando django
    python3.11
    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()

## Boa Prática
    - Utilização da lib dotenv ou mesmo definir a variavel no compose no environment.
    
    Por exemplo no compose:

    version: '3'
    services:
    web:
        image: my_django_app
        ports:
        - "8000:8000"
        environment:
        - SECRET_KEY=sua_chave_secreta_aqui

    referenciado ela no settings.py:
    SECRET_KEY = os.environ.get('SECRET_KEY')