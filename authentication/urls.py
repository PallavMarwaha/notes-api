from django.urls import path
from rest_framework.authtoken import views
from .views import RegisterView

app_name = "authentication"


urlpatterns = [
    path("login", views.obtain_auth_token, name="login"),
    path("register", RegisterView.as_view(), name="register"),
]
