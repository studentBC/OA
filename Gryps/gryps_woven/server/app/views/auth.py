# Create your views here.

import jwt

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from server.settings import JWT_SECRET
from app.models import User
from app.serializers import AuthUserSerializer
from app.serializers import UserSerializer


class AuthViewSet(ViewSet):
    @action(methods=["post"], detail=False, authentication_classes=[])
    def login(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = User.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            return Response({"message": "Unauthorized"}, status=401)

        token = jwt.encode(
            {"id": user.id, "email": user.email}, JWT_SECRET, algorithm="HS256"
        )

        serializer = AuthUserSerializer({"user": user, "token": token})
        return Response(serializer.data)

    @action(methods=["post"], detail=False, authentication_classes=[])
    def register(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        user = User.objects.create(
            email=email, first_name=first_name, last_name=last_name
        )
        user.set_password(password)
        user.save()

        token = jwt.encode(
            {"id": user.id, "email": user.email}, JWT_SECRET, algorithm="HS256"
        )

        serializer = AuthUserSerializer({"user": user, "token": token})
        return Response(serializer.data)

    @action(methods=["get"], detail=False)
    def me(self, request):
        if request.user.is_authenticated:
            return Response(UserSerializer(request.user).data)
        return Response()
