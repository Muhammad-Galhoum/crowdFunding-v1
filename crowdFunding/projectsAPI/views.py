from rest_framework.views import APIView
from projects.models import Project
from .serializers import Projectser
from rest_framework.response import Response


# Create your views here.


class Projectview(APIView):
    def get(self, request):
        projects = Project.objects.all()
        ser = Projectser(projects, many=True)
        return Response(ser.data)

