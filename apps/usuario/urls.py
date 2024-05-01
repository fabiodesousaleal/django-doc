from django.urls import path
from .views import *
urlpatterns=[ 
    path('', index, name='index'),   
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro-user')
]