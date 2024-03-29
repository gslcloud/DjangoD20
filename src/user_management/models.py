from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name_plural = "Users"


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField('Permission')

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar_image = models.ImageField(upload_to='avatars/')
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username


class Organization(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="organizations")
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name