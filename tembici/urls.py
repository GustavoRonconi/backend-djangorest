from django.urls import path
from tembici import views

urlpatterns = [
    path("", views.login, name="login")
]
