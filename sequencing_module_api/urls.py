from . import views
from django.urls import path



urlpatterns  = [

    path("user", views.UserList.as_view()),
    path("user/<int:pk>", views.UserDetail.as_view()),
]