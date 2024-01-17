from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path('search-woj', views.searchWojew, name="search_woj"),
    path('search-woj/<int:woj_id>', views.showWojew, name='show_woj'),
    path('create-woj/', views.createWojew, name='create_woj'),

    path('search-pow', views.searchPowiat, name="search_pow"),
    path('search-pow/<int:woj_id>', views.showPowiat, name='show_pow'),
    path('create-pow/', views.createPowiat, name='create_pow'),
    
    path('search-gmi', views.searchGmina, name="search_gmi"),
    path('search-gmi/<int:woj_id>', views.showGmina, name='show_gmi'),
    path('create-gmi/', views.createGmina, name='create_gmi'),
]