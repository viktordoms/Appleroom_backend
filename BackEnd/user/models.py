from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser повинен мати is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser повинен мати is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('Ви повинні ввести email'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name


class Category(models.Model):
    title = models.CharField("Категорія", max_length=150)
    description = models.TextField("Опис", blank=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Number(models.Model):
    number = models.CharField("Номер", max_length=50)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номери"


class City(models.Model):
    title = models.CharField("Місто", max_length=50)
    slug = models.SlugField(max_length=160, unique=True)
    number = models.ManyToManyField(
        Number, verbose_name="Номер", null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Місто"
        verbose_name_plural = "Міста"


