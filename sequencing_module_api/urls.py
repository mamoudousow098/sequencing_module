from . import views
from django.urls import path



urlpatterns  = [

    path("user", views.UserList.as_view()),
    path("user/<int:pk>", views.UserDetail.as_view()),

    path("ordinateur", views.OrdinateurList.as_view()),
    path("ordinateur/<str:pk>", views.OrdinateurDetail.as_view()),
]