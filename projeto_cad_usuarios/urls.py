
from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referencia
    path('', views.home, name='home'),

    #usuarios.com/usuarios

    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
