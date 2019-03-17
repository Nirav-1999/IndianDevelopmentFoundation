from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from .models import Student

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email',) 
 
        
class StudentDataForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user',)
        fields = ('age', 'state', 'caste', 'income', 'resume', 'university_name', 'gender', 'birthdate')
