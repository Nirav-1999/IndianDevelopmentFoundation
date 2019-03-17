from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index/", user)
    else:
        form = AuthenticationForm()
    return render (request, "github/login.html", {"form" : form})


def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect("github:logout")
    else:
        return render(request, "github/logout.html")

# class LoginApiView(APIView):
#     permission_classes = (AllowAny,)
#     def get(self,request):
#         content = {
#             'user': str(request.user),
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)

#     def post(self,request):
#         user = authenticate(username = request.query_params['username'], password = request.query_params['password'])
#         print(user)
#         if user is not None:
#             print("hi")
#             login(request,user)
#         return Response({'user':'Hi'})


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

# class LoginApiView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = authenticate(
#                 username=serializer.data.get("username"),
#                 # password=serializer.data.get("password"),
#             )
#             login(request, user)
#             return HttpResponseRedirect(redirect_to="/menus/")
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# class Logout(APIView):
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         logout(request)
#         return HttpResponseRedirect(redirect_to="/login/")
