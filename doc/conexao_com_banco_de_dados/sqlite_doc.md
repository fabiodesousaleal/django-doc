# Requisitos 
    Em uma instalação padrão já vem configurado.
# Alteração no settings.py
    DATABASES = {
        'default': {        
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',      
        }
    }