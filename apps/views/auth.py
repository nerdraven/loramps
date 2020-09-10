from rest_framework import generics
from knox.models import AuthToken
from knox.views import Response

from .serializers import (
    RegisterSerializer, LoginSerializer, UserSerializer,
)
# Register API
class RegisterAPI(generics.GenericAPIView):
    ''' Register The User and return the user with an authtoken '''

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user' : RegisterSerializer(user, context=self.get_serializer_context()).data ,
            'token' : AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(generics.GenericAPIView):
    ''' This Login the User to the Website and return an authtoken '''

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user' : UserSerializer(user, context=self.get_serializer_context()).data,
            'token' : AuthToken.objects.create(user)[1]
        })


# User API
class UserAPI(generics.RetrieveAPIView):
    ''' Retrieves the User with the users authtoken '''

    serializer_class = UserSerializer

    def get_object(self):
        token_key = self.request.headers.get('Authorization', None)
        if token_key:
            print(token_key.split(' '))
            token_key = token_key.split(' ')[1]
            try:
                auth = AuthToken.objects.get(token_key=token_key[:8])
            except AuthToken.DoesNotExist:
                raise
            return auth.user
        return self.request.user