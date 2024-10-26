import os
import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def normalize_email(self, email):
        if email is not None:
            return email.lower()

    def _create_user(
        self,
        username: str,
        password: str,
        email: str = None,
        telegram: str = None,
        is_staff: bool = False,
        is_superuser: bool = False,
    ) -> 'User':

        email = self.normalize_email(email)
        user: 'User' = self.model(username=username,
                                  email=email,
                                  telegram=telegram,
                                  is_staff=is_staff,
                                  is_superuser=is_superuser)
        user.set_password(password)
        user.save()

        return user

    def create_user(
            self,
            username: str,
            password: str,
            email: str = None,
            telegram: str = None,
            is_staff: bool = False,
    ) -> 'User':

        return self._create_user(username,
                                 password,
                                 email=email,
                                 telegram=telegram,
                                 is_staff=is_staff)

    def create_superuser(self, username: str, password: str) -> 'User':
        return self._create_user(username, password, is_staff=True, is_superuser=True)


def user_pic_path(instance, filename):
    return os.path.join(instance.__class__.__name__, filename)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(unique=True, verbose_name=_('Username'))
    email = models.EmailField(blank=True, null=True, unique=True, verbose_name=_('Email'))
    telegram = models.EmailField(blank=True, null=True, unique=True, verbose_name=_('Telegram'))
    avatar = models.ImageField(upload_to=user_pic_path, default='img/no_photo_300_200.jpg', verbose_name=_('avatar'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Is staff'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Date joined'))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()
