from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class LoginApiView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),  # None
        }
        return Response(content)
    
    def post(self,request):
        user = authenticate(username = request.query_params['username'], password = request.query_params['password'])
        print(user)
        if user is not None:
            print("hi")
            login(request,user)
        return Response({'user':'Hi'})


        # if user:
        #     print(user.password)
        #     if user.password == request.query_params['password']:
        #         login(request,user)
        #     else:
        #         print('wrong password')
        # else:
        #     print('user does not exist')
        


# class MyBasicAuthentication(BasicAuthentication):

#     def authenticate(self, request):
#         user, _ = super(MyBasicAuthentication, self).authenticate(request)
#         print("hi")
#         login(request, user)
#         print('welcome')
#         return user, _


# class ExampleView(APIView):
#     authentication_classes = (SessionAuthentication, MyBasicAuthentication)
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)