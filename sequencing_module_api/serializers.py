from rest_framework import serializers
from .models import *


class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta :
        model = User 
        fields = ['email', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data) :
        password = validated_data.pop('password', None) 
        instance = self.Meta.model(**validated_data)
        if password is not None :
            instance.set_password(password)
        instance.save()
        return instance



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
        model = Run
        fields = "__all__"

class AnalyseSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Analyse
        fields = "__all__"

class EchantillonSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Echantillon
        fields = "__all__"

class DossierZipSerializer(serializers.ModelSerializer) :
    class Meta:
        model = DossierZip 
        fields = "__all__"