# Create your views here.

from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializers import AuditSerializer
from app.db_helper import namedtuplefetchall


class AuditListView(APIView):

    def post(self, request):
        filters = request.data.get("q", {}).get("filters", {})
        rows = []
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    SELECT *
                    FROM app_audit
                    where message ILIKE %s
                """,
                [f"%{filters.get('message')}%"]
            )
            rows = namedtuplefetchall(cursor, 'Audit')

        return Response(AuditSerializer(rows, many=True).data)
