from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .serializers import *
# Create your views here.

# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
class MyUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        print("USER IS " , user)
        serializer = CustomUserSerializer(user)
        print(user.role)
        return Response(serializer.data)
