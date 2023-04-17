from rest_framework import serializers

from app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name")


class AuthUserSerializer(serializers.Serializer):
    user = UserSerializer()
    token = serializers.CharField()
