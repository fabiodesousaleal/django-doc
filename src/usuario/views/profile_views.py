from django.utils import timezone
def get_upload_to(instance, filename):
    user_id = instance.user.id
    now = timezone.now()
    year = now.strftime('%Y')
    diretorio = f"imagens/profile/{year}/"
    nome_do_arquivo = f'profile{user_id}.jpg'
    return f'{diretorio}{nome_do_arquivo}'