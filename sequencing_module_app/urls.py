from django.urls import path
from sequencing_module_app import views



urlpatterns = [
    path("home", views.home_view),

    path("", views.login_view),

    path("file", views.file_view),

    path("test", views.test_view)
]