from django.shortcuts import redirect
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.conf import settings  # Import settings from Django
from allauth.account.utils import complete_signup
from allauth.account.models import EmailAddress

from allauth.account.views import EmailVerificationSentView
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.save()
            
            if user:
                #EmailAddress.objects.get_or_create(user=user)
                complete_signup(
                        self.request._request, user,
                        settings.ACCOUNT_EMAIL_VERIFICATION,
                        None,
                    )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        super().create


class AuthViewSet(ViewSet):
    permission_classes=[AllowAny]
  
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            email = EmailAddress.objects.filter(user=user).first()
            if not  email.verified:
                return Response({'error':'verify tour email'}, status=status.HTTP_401_UNAUTHORIZED)

            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class EmailVerification(EmailVerificationSentView):
    ...

def redirect_to_react(request):


    return redirect("http://127.0.0.1:3000")