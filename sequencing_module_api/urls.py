from . import views
from django.urls import path, re_path



urlpatterns  = [

    path("user", views.UserList.as_view()),
    path("user/<int:pk>", views.UserDetail.as_view()),

    path("search/user=<str:user_name>", views.SearchUserByName().as_view()),

    path("token", views.JSONWebTokenAuth().as_view()),

    path("ordinateur", views.OrdinateurList.as_view()),
    path("ordinateur/<str:pk>", views.OrdinateurDetail.as_view()),
    
    path("run", views.RunList.as_view()),
    path("run/<int:pk>", views.RunDetail.as_view()),
    
    path("fichier", views.FichierList.as_view()),
    path("fichier/<int:pk>", views.FichierDetail.as_view()),

    path("echantillon", views.EchantillonList.as_view()),
    path("echantillon/<int:pk>", views.EchantillonDetail.as_view()),

    path("dossierzip", views.DossierZipList.as_view()),
    path("dossierzip/<int:pk>", views.DossierZipDetail.as_view()),
    
    path("analyse", views.AnalyseList.as_view()),
    path("analyse/<int:pk>", views.AnalyseDetail.as_view()),

]