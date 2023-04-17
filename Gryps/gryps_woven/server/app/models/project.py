from django.db import models
from app.models import User


class Project(models.Model):
    title = models.TextField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
