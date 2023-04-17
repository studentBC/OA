from django.db import models
from app.models import User


class Audit(models.Model):
    event = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    context = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['event', ]),
            models.Index(fields=['status', ]),
        ]
