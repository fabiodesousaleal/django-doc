from django.db import models
from django.contrib.auth.models import User
from apps.usuario.views.profile_views import get_upload_to


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=get_upload_to, null=True, blank=True)
    descricao = models.TextField(max_length=255, null=True, blank=True)