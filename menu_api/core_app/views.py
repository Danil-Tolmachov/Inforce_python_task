from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core_app.serializers import RestaurantSerializer, MenuSerializer
from . import services


class GetTodaysMenu(APIView):
    def get(self, request):
        menu = services.get_todays_menus()
        serializer = MenuSerializer(data=menu, many=True)
        serializer.is_valid()

        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class GetTodaysResults(APIView):
    def get(self, request):
        menu = services.get_choosen_menu()
        return Response(data=menu.items, status=status.HTTP_200_OK)


class CreateRestaurant(APIView):
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadRestaurantMenu(APIView):
    def post(self, request):
        restaurant_id = request.query_params['restaurant']
        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid():
            if services.update_menu(restaurant_id, serializer.validated_data):
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
