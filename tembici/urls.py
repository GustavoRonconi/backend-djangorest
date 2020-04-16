from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from tembici import views

urlpatterns = [
    path("", auth_views.login, name="login"),
    
]
