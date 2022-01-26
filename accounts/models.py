from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import MyUserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=150, unique=True)
    objects = MyUserManager()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name',)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
