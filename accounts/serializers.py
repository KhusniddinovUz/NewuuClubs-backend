from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "first_name", "last_name", "username", "email", "group_number", "student_id",
            "student_year")


class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data["username"],
                                        email=validated_data["email"],
                                        password=validated_data["password"],
                                        first_name=validated_data["first_name"],
                                        last_name=validated_data["last_name"])
        return user


class AccountLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")
