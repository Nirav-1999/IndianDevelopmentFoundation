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
from .crawl import gather_links
from .forms import StudentDataForm, UserCreationForm
import random

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
def login_page(request):
    if request.user:
        return render(request, "landing.html", {"form" : "form"})

    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        print(form)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, "landing.html", {"form" : "form"})
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form" : form})


def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect("Student:logout")
    else:
        return render(request, "index.html")

# class SearchScholarshipsAPIView(APIView):
    

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

class ScholarshipView(APIView):
    permission_classes = (AllowAny,)

    def get(self,request):
        a = gather_links('https://www.buddy4study.com/','https://www.buddy4study.com/scholarships')
        for elements in a:
            elements.update({'prize':(random.randint(1,10)*1000)})
        return Response(a)

def add_student(request):
    user_form = {}
    profile_form ={}
    
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = StudentDataForm(request.POST)
        print(profile_form)
            
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            
            # import pdb; pdb.set_trace()
            # print(college)
            student = profile_form.save(commit = False)
            student.user = user
        
            print("Done")
            profile_form.save()
            return redirect('Student:login')
        else:
            print(profile_form.errors)
            print(user_form.errors)
            user_form = UserCreationForm()
            profile_form = StudentDataForm()
           

            
    return render(request,'SignUp.html',{'user_form':user_form,'profile_form':profile_form})