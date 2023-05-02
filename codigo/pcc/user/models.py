from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils import timezone
import re
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class Usuario(AbstractUser, PermissionsMixin):
    username = models.CharField(('username'), max_length=15, unique=True, help_text=('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'), ('Enter a valid username.'), ('invalid'))])
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    email = models.EmailField(('email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(('staff status'), default=False, help_text=('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(('active'), default=True, help_text=('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_superuser = models.BooleanField(('active'), default=False)
    choose_ong = models.BooleanField(('ong'), default=False)

    telefone = models.CharField(max_length=15, blank=False, null=True)
    imagem = models.ImageField(upload_to='static/imagens/perfil/', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

   
