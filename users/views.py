from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# from .serializer import UserSerializer
# from rest_framework import generics
# from rest_framework import permissions
# from .models import Product, Task



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        message = {
            'message': 'hello world'
        }
        return Response(message)
    

class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
            # "Result": "Registeration was successfull!"
        })