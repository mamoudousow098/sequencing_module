from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class OrdinateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordinateur
        fields = "__all__"

class FichierSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Fichier
        fields = "__all__"


class RunSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Fichier
        fields = "__all__"

class EchantillonSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Fichier
        fields = "__all__"

class DossierZipSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Fichier 
        fields = "__all__"