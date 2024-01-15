from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path('search-woj', views.searchWojew, name="search-woj"),
]