from django import forms
from .models import Usuarios
class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, max_length=50 )
    class Meta:
        model = Usuarios
        fields = ['nome', 'apelido', 'nascimento', 'email', 'senha', 'foto', 'inativo']

    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    # nome = models.CharField(max_length=255)
    # apelido = models.CharField(max_length=255, blank=True, null=True)
    # nascimento = models.DateField(verbose_name='Data de Nascimento', null=True, blank=True)
    # data_cadastro = models.DateField(verbose_name='Data de Cadastro', auto_now = True )
    # email = models.EmailField(u'e-mail',max_length=255)
    # senha = models.CharField(u'senha', max_length=50 )
    # foto = models.ImageField(upload_to='fotos_usuarios', null=True, blank=True)
    # inativo = models.BooleanField(default=False