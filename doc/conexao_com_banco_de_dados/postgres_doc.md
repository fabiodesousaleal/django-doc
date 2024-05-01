# Requisitos 
    pip install psycopg2-binary
# Alteração no settings.py no core do projeto
    DATABASES = {
        'default': { 
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mydatabase',
            'USER': 'myuser',
            'PASSWORD': 'mypassword',
            'HOST': 'localhost',  # nome ou endereço do servidor database
            'PORT': '5432',
        }
    }