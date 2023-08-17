from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import AccountSerializer, AccountLoginSerializer, AccountRegisterSerializer
from drf_standardized_errors.handler import exception_handler
from .models import User


class RegisterAPI(generics.GenericAPIView):
    serializer_class = AccountRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": AccountSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

    def get_exception_handler(self):
        return exception_handler


class LoginAPI(generics.GenericAPIView):
    serializer_class = AccountLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user': AccountSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


class UserUpdateAPI(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
