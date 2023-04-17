# Create your views here.

from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Project
from app.serializers import ProjectSerializer
from app.db_helper import namedtuplefetchall
from app.db_helper import namedtuplefetchone


class ProjectListView(APIView):
    def post(self, request):
        if not len(request.data):
            raise Exception("No row data given")

        title = request.data.get("title")
        description = request.data.get("description")

        project = Project.objects.create(
            title=title, description=description, owner_id=request.user.id
        )
        return Response(ProjectSerializer(project).data)

    def get(self, request):
        rows = []
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    SELECT p.*,
                    u.email AS owner
                    FROM app_project p
                    LEFT JOIN auth_user u ON p.owner_id=u.id
                """
            )
            rows = namedtuplefetchall(cursor, 'Project')

        return Response(ProjectSerializer(rows, many=True).data)


class ProjectDetailView(APIView):
    def get(self, request, id=None):
        row = None
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    SELECT p.*,
                    u.email AS owner
                    FROM app_project p
                    LEFT JOIN auth_user u ON p.owner_id=u.id
                    WHERE p.id=%s
                """,
                [id],
            )
            row = namedtuplefetchone(cursor, 'Project')

        return Response(ProjectSerializer(row).data)

    def put(self, request, id=None):
        if not id or type(id) != int:
            raise Exception("No id given")

        title = request.data.get("title")
        description = request.data.get("description")

        project = Project.objects.filter(id=id).first()
        project.title = title
        project.description = description
        project.save()

        return Response(ProjectSerializer(project).data)

    def delete(self, request, id=None):
        if not id or type(id) != int:
            raise Exception("No id given")

        project = Project.objects.filter(id=id).first()
        ser_data = ProjectSerializer(project).data

        if project:
            project.delete()
        return Response(ser_data)
