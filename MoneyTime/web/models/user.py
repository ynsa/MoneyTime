# system
import os
import uuid

# django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# local
from MoneyTime.web.managers import UserManager


class User(AbstractUser):

    # username = None

    username = models.CharField(
        _('Username'),
        max_length=50,
        unique=False,
        null=True
    )
    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)

    # @property
    # def is_staff(self):
    #     return self.is_superuser

    REQUIRED_FIELDS = [
        'username',
    ]

    USERNAME_FIELD = 'email'

    def __str__(self):
        return '{0}({1})'.format(self.email, self.username)
        # return '{0}'.format(self.email)

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
