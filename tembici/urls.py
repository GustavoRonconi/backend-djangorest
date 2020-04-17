from django.urls import path
from tembici import views

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
]
