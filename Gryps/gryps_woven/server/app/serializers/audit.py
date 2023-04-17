from rest_framework import serializers

from app.models import Audit


class AuditSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = Audit
        fields = ("__all__")
        depth = 1
