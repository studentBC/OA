# Create your views here.

from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
from app.db_helper import dictfetchall


class SettingListView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    SELECT u.daily_email_updates AS daily_email_updates
                    FROM auth_user u
                    WHERE u.id = %s
                """,
                [request.user.id]
            )
            rows = dictfetchall(cursor)

            return Response(rows)


class SettingDetailView(APIView):
    def put(self, request, setting_name=None):
        value = request.data.get("value")
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
                    UPDATE auth_user
                    SET {setting_name}=%s
                    WHERE auth_user.id=%s
                """,
                [value, request.user.id]
            )

            return Response()
