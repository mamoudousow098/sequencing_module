from django.urls import path, re_path
from sequencing_module_api import views



urlpatterns  = [

    path("user", views.UserList.as_view()),
    path("user/<int:pk>", views.UserDetail.as_view()),

    #path("search/user=<str:user_name>", views.SearchUserByName().as_view()),

    path("token", views.JSONWebTokenAuth().as_view()),

    path("sequenceur", views.SequenceurList.as_view()),
    path("sequenceur/<str:pk>", views.SequenceurDetail.as_view()),
    
    path("run", views.RunList.as_view()),
    path("run/<int:pk>", views.RunDetail.as_view()),

    path("folder", views.FolderList.as_view()),
    path("folder/<int:pk>", views.FolderDetail.as_view()),

    path("send", views.DoSomethingOnServer.as_view()),

    path("ftp", views.FtpDownload.as_view()),

    path("fichier", views.FichierList.as_view()),
    path("fichier/<int:pk>", views.FichierDetail.as_view()),

    path("echantillon", views.EchantillonList.as_view()),
    path("echantillon/<int:pk>", views.EchantillonDetail.as_view()),

    path("dossierzip", views.DossierZipList.as_view()),
    path("dossierzip/<int:pk>", views.DossierZipDetail.as_view()),
    
    path("analyse", views.AnalyseList.as_view()),
    path("analyse/<int:pk>", views.AnalyseDetail.as_view()),

]