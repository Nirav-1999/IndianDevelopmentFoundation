from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER = [
    ("M", ("Male")),
    ("F", ("Female")),
    ("O", ("Other")),

]

CASTES = [
    ("SC", ("SC")),
    ("ST", ("ST")),
    ("OBC", ("OBC")),
    ("NT", ("NT")),
    ("Open", ("Open")),

]


STATES = [
    ("Andhra Pradesh", ("Andhra Pradesh")),
    ("Arunachal Pradesh", ("Arunachal Pradesh")),
    ("Assam", ("Assam")),
    ("Bihar", ("Bihar")),
    ("Chhattisgarh", ("Chhattisgarh")),
    ("Goa", ("Goa")),
    ("Gujarat", ("Gujarat")),
    ("Haryana", ("Haryana")),
    ("Himachal Pradesh", ("Himachal Pradesh")),
    ("Jammu and Kashmir", ("Jammu and Kashmir")),
    ("Jharkhand", ("Jharkhand")),
    ("Karnataka", ("Karnataka")),
    ("Kerala", ("Kerala")),
    ("Madhya Pradesh", ("Madhya Pradesh")),
    ("Maharashtra", ("Maharashtra")),
    ("Manipur", ("Manipur")),
    ("Meghalaya", ("Meghalaya")),
    ("Mizoram", ("Mizoram")),
    ("Nagaland", ("Nagaland")),
    ("Odisha", ("Odisha")),
    ("Punjab", ("Punjab")),
    ("Rajasthan", ("Rajasthan")),
    ("Sikkim", ("Sikkim")),
    ("Tamil Nadu", ("Tamil Nadu")),
    ("Telangana", ("Telangana")),
    ("Tripura", ("Tripura")),
    ("Uttar Pradesh", ("Uttar Pradesh")),
    ("Uttarakhand", ("Uttarakhand")),
    ("West Bengal", ("West Bengal")),



]

class Student(models.Model):
    user = models.OneToOneField(User,related_name = 'student', on_delete=models.CASCADE,primary_key=True)
    age = models.PositiveIntegerField()
    state = models.CharField(choices = STATES, default = "None", blank = False, max_length = 100)
    caste = models.CharField(choices = CASTES, default = "None", blank = False, max_length = 100)
    income = models.PositiveIntegerField()
    resume = models.FileField()
    university_name = models.CharField(max_length = 100)
    gender = models.CharField(choices = GENDER,default = "None", blank = False, max_length = 100)
    birthdate = models.DateField()

    def __str__(self):
        return self.user.username
