from django.urls import path
from . import views

# URLConfiguration
urlpatterns = [
    path("hello/", views.HelloView.as_view())
]