from django.urls import path
from tennis import views

urlpatterns = [
    path("home", views.home),
    path("about",views.about)
]