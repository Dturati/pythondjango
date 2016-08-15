import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.conf import settings


class User(AbstractBaseUser, PermissionsMixin):
    username    =   models.CharField(
        'Nome de usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O nome de usuário só pode conter letras, digitos ou ','invalid')]
        )
    email       =   models.EmailField('Email',unique=True)
    name    =   models.CharField('Nome',max_length=100, blank=True,default=True)
    is_active   =   models.BooleanField('Está ativo?',blank=True,default=True)
    is_staff    =   models.BooleanField('É da equipe', blank=False,default=True)
    date_joined =   models.DateTimeField('Data de Entrada',auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name        = 'Usuario'
        verbose_name_plural =  'Usuários'

class PasswordReset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
            verbose_name='Usuário',
            related_name='resets' #não cria o atributio padrão, cria o atruibuto resets
    ) #Relacionamento

    key = models.CharField('Chave',max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)

    #black campo não obrigatório
    confirmed = models.BooleanField('Confirmado?',default=False,blank=True)  #se o link já foi usado
    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Reset senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at'] #ordenaão