# Generated by Django 2.0.2 on 2018-02-22 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('apelido', models.CharField(blank=True, max_length=255, null=True)),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('data_cadastro', models.DateField(verbose_name='Data de Cadastro')),
                ('email', models.EmailField(max_length=255)),
                ('senha', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_usuarios')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]