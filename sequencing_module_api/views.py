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

class FichierList(generics.ListCreateAPIView):
    queryset = Fichier.objects.all()
    serializer_class = FichierSerializer


class FichierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fichier.objects.all()
    serializer_class = FichierSerializer


class RunList(generics.ListCreateAPIView) :
    queryset = Run.objects.all()
    serializer_class = RunSerializer

class RunDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fichier.objects.all()
    serializer_class = RunSerializer


class EchantillonList(generics.ListCreateAPIView) :
    queryset = Echantillon.objects.all()
    serializer_class = EchantillonSerializer

class EchantillonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fichier.objects.all()
    serializer_class = EchantillonSerializer

class DossierZipList(generics.ListCreateAPIView) :
    queryset = DossierZip.objects.all()
    serializer_class = DossierZipSerializer

class DossierZipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DossierZip.objects.all()
    serializer_class = DossierZipSerializer


