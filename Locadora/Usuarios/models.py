from django.db import models
from django.contrib.auth.models import User


class Usuarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False)

    nome = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255, blank=True, null=True)
    nascimento = models.DateField(verbose_name='Data de Nascimento', null=True, blank=True    )
    data_cadastro = models.DateField(verbose_name='Data de Cadastro')
    email = models.EmailField(max_length=255)
    senha = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos_usuarios', null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

