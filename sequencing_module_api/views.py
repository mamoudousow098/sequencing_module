from django.conf import settings

from rest_framework import generics
from rest_framework import parsers, renderers, status
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .models import *
from .serializers import *
from .authentication import JSONWebTokenAuthentication

import datetime
import jwt

# Create your views here.
        

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class JSONWebTokenAuth(generics.GenericAPIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            return Response({
                "message": "User not found",
                "success": "False"
            }, status = status.HTTP_404_NOT_FOUND)
        
        if not user.check_password(password) :
            return Response({
                "message": "incorrect password",
                "success": "False"
            }, status = status.HTTP_404_NOT_FOUND)

        token = jwt.encode({
                'email': user.email,
                'iat': datetime.datetime.utcnow(),
                'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }, settings.SECRET_KEY, algorithm="HS256")
        response = Response()
        response.set_cookie(key='token', value=token, httponly=True)
        response.data = {
            'token' : token
        }
        return response


    def get(self, request) :
        token = request.COOKIES.get('token')
        
        auth = JSONWebTokenAuthentication()
        
        data = auth.authenticate_credentials(token)
        user = data[0]
        payload = data[1]

        userSerializer = UserSerializer(user)

        return Response({
            "message" : "success",
            "payload" : payload,
            "data" : userSerializer.data
        })
        
       

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


class AnalyseList(generics.ListCreateAPIView) :
    queryset = Run.objects.all()
    serializer_class = AnalyseSerializer

class AnalyseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fichier.objects.all()
    serializer_class = AnalyseSerializer


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


