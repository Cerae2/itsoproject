from rest_framework import generics
from ..models import Login
from .serializers import LoginSerializer

class Login(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
