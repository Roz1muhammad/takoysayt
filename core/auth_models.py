from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManger(UserManager):


    def create_user(self,phone, username, password=None, **extra_fields):
        if not username:
            raise ValueError("foydalanvchi ism mavjude emas ")
        user = self.model(phone=phone ,username=username, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self,phone, username, password=None, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        return self.create_user(phone, username, password=password, **kwargs)


class User(AbstractUser):
    username = models.CharField(max_length=56, unique=True)
    phone = models.CharField(max_length=56)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
jkl;
    email = False
    last_name = False
    first_name = False

    objects = CustomUserManger()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone"]








