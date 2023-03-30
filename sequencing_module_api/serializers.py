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
        # fields = [field.name for field in User._meta.get_fields()]
        # fields.remove('logentry')
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
    

class FichierSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Fichier
        fields = "__all__"

class EchantillonSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Echantillon
        fields = "__all__"

class RunSerializer(serializers.ModelSerializer) :
    run_fichiers = FichierSerializer(many=True, read_only=True)
    echantillons = EchantillonSerializer(many=True, read_only=True)
    class Meta:
        model = Run
        fields = '__all__'
        #fields = [field.name for field in User._meta.get_fields()]

class FolderChildrenSerializer(serializers.ModelSerializer) :
    fichiers = FichierSerializer(many=True, read_only=True)
    children = serializers.PrimaryKeyRelatedField(many=True, queryset=Folder.objects.all())

    def to_representation(self, instance):
        self.fields['children'] = FolderChildrenSerializer(many=True, read_only=True)
        return super(FolderChildrenSerializer, self).to_representation(instance)
    #children = serializers.StringRelatedField(many=True)
    class Meta :
        model = Folder
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer) :

    fichiers = FichierSerializer(many=True, read_only=True)
    children = FolderChildrenSerializer(many=True, read_only=True)
    class Meta:
        model = Folder
        fields = '__all__'
class SequenceurSerializer(serializers.ModelSerializer):

    runs =  RunSerializer(many=True, read_only=True)
    class Meta:
        model = Sequenceur
        fields = '__all__'
class AnalyseSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Analyse
        fields = "__all__"


class DossierZipSerializer(serializers.ModelSerializer) :
    class Meta:
        model = DossierZip 
        fields = "__all__"
