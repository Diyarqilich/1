from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.text import slugify

class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None, **extra_fields):
        if not username:
            raise ValueError('Имя пользователя (username) должно быть указано')
        if not phone_number:
            raise ValueError('Номер телефона должен быть указан')
        
        user = self.model(
            username=username,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(username, phone_number, password, **extra_fields)


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    bio = models.TextField(blank=True)
    cat_breed = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}--{self.last_name}") if self.first_name or self.last_name else slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username