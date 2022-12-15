from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
    

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    about = models.CharField(max_length=500, blank=True)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

class UserFollowed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_followed")
    followed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email