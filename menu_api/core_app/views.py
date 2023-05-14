from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class Test(APIView):
    
    def get(self, request, *args, **kwargs):
        version = request.version
        print(version)
        return Response(data={'success': version})
