from django.db import models
from django.contrib.auth.models import AbstractUser

from app.managers import UserManager

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    daily_email_updates = models.BooleanField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "auth_user"
