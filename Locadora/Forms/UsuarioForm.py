from django import forms

class UsuarioForm(forms.Form ):

    nome = forms.CharField(label='Nome', max_lenght=100 )
    apelido = forms.CharField(label='Apelido', max_lenght=100)
    nascimento = forms.DateField(label='Nascimento')
    email = forms.EmailField(label='e-mail', max_lenght=100)
    #
    # nome = models.CharField(max_length=255)
    # apelido = models.CharField(max_length=255, blank=True, null=True)
    # nascimento = models.DateField(verbose_name='Data de Nascimento', null=True, blank=True    )
    # data_cadastro = models.DateField(verbose_name='Data de Cadastro')
    # email = models.EmailField(max_length=255)
    # senha = models.CharField(max_length=50)
    # foto = models.ImageField(upload_to='fotos_usuarios', null=True, blank=True)
    # inativo = models.BooleanField(default=False)
    #
