from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .custom_user_manager import CustomUserManager


# Create your models here.

class UserType(models.Model):
    userTypeName = models.TextField(max_length=200, unique=True)
    userTypeNameBan = models.TextField(max_length=200)

    def __str__(self):
        return self.userTypeName


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.TextField(max_length=50, unique=True)
    phone = models.TextField(max_length=11, unique=True)
    email = models.EmailField(_("email address"), unique=True)

    userType = models.ForeignKey(UserType, on_delete=models.SET_NULL, blank=True, null=True)

    is_staff = models.BooleanField(default=0)
    is_superuser = models.BooleanField(default=0)
    is_active = models.BooleanField(default=0)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

