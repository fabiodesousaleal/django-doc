def sqlite(BASE_DIR: str)->dict:
    return {
        'default': {        
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',      
        }
    }

def postgres()->dict:
    return {
        'default': { 
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mydatabase',
            'USER': 'myuser',
            'PASSWORD': 'mypassword',
            'HOST': 'localhost',  # nome ou endereço do servidor database
            'PORT': '5432',
        }
    }