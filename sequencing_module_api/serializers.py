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