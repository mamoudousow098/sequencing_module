from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrdinateurList(generics.ListCreateAPIView):
    queryset = Ordinateur.objects.all()
    serializer_class = OrdinateurSerializer


class OrdinateurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ordinateur.objects.all()
    serializer_class = OrdinateurSerializer