# django
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Custom User Manager."""

    def create_user(self, username=None,  email=None, password=None):
        """
        Creates and saves a User with the given email, password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given username,
        email and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user
