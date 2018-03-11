
from django.urls import path
from .views import listarUsuarios, incluirUsuario, atualizarUsuario, deletarUsuario

urlpatterns = [
    path('listar/', listarUsuarios, name="listar" ),
    path('incluir/', incluirUsuario, name="incluir"),
    path('alterar/<int:id>/', atualizarUsuario, name="alterar"),
    path('deletar/<int:id>/', deletarUsuario, name="deletar"),
]
