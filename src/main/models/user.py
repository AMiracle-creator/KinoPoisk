from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager
from django.core.files import File
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from main.models.base import BaseModel
from main.models.movie import Movie


class UserManager(DjangoUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.model(email=email, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class Role(DjangoChoices):
    admin = ChoiceItem()
    user = ChoiceItem()


class KinopoiskUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(unique=True)
    img = models.ImageField(upload_to='users_img/')
    role = models.CharField(choices=Role.choices, default=Role.user, max_length=50)
    name = models.CharField(unique=True, max_length=15, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_staff(self):
        return self.is_superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
