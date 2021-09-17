from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.db import models


# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, name, email, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(name, email, password, **other_fields)

    def create_user(self, name, email, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('full Name'), max_length=100)
    email = models.EmailField(_('email address'),unique=True)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','dob']

    def __str__(self):
        return self.name


    @property
    def is_eligible(self):
        return False if self.vote_set.all().exists() else True
