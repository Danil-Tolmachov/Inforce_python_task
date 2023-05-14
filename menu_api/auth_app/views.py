from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from core_app.models import Menu
from auth_app.serializers import EmployeeSerializer


class CreateUser(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteFor(APIView):
    def get(self, request):
        menu_id = request.query_params['menu']

        try:
            menu_obj = Menu.objects.get(pk=menu_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        menu_obj.vote(request.user)
        return Response(status=status.HTTP_200_OK)
