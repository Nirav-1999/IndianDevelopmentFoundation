from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")



class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=False)

    class Meta:
        model = Student
        fields = ('age', 'state', 'caste', 'income', 'resume', 'university_name', 'gender', 'birthdate', 'user')

    def create(self, validated_data):
        user = User(
            first_name=validated_data["user"]["first_name"],
            last_name=validated_data["user"]["last_name"],
            email=validated_data["user"]["email"],
            username=validated_data["user"]["username"],
        )
        user.set_password(validated_data["user"]["password"])
        user.save()
        student = Student(user=user, age=validated_data["age"], state=validated_data["state"], caste=validated_data["caste"], income=validated_data["income"], resume=validated_data["resume"], university_name=validated_data["university_name"],gender=validated_data["gender"],birthdate=validated_data["birthdate"])
        student.save()
        return student

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(style={"input_type": "password"})
