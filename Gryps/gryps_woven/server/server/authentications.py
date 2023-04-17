import jwt
from app.models import User
from rest_framework import authentication
from rest_framework import exceptions

from server.settings import JWT_SECRET


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION')
        try:
            token = authorization.split(" ")[1]
            user_id = jwt.decode(token, JWT_SECRET, algorithms=[
                                 "HS256"]).get("id")
            user = User.objects.get(id=user_id)
        except Exception:
            raise exceptions.AuthenticationFailed()
        return (user, None)

    def authenticate_header(self, request):
        return "Bearer"
