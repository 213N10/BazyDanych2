from django.urls import path, include

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path("", include("django.contrib.auth.urls")),
    path("wyszukaj-all", views.wyszukajAll, name = "wyszukaj_all"),
    
    path("admin-danych-main", views.adminDanychMain, name = "admin_danych_main"),
    path("edycja-gmina", views.edycjaGmina, name = "edycja_gmina"),
    path('edycja-powiat', views.edycjaPowiat, name = 'edycja_powiat'),
    path('edycja-woj', views.edycjaWoj, name='edycja_woj'),
    
    path('search-woj/', views.searchWojew, name="search_woj"),
    path('search-woj/<int:woj_id>', views.showWojew, name='show_woj'),
    path('create-woj/', views.createWojew, name='create_woj'),
    path('display-woj/', views.displayWojew, name='display_woj'),
    path('update-woj/<int:woj_id>/', views.updateWojew, name='update_woj'),

    path('search-pow/', views.searchPowiat, name="search_pow"),
    path('search-pow/<int:woj_id>', views.showPowiat, name='show_pow'),
    path('create-pow/', views.createPowiat, name='create_pow'),
    path('display-pow/', views.displayPowiat, name='display_pow'),
    path('update-pow/<int:woj_id>/', views.updatePowiat, name='update_pow'),
    
    path('search-gmi/', views.searchGmina, name="search_gmi"),
    path('search-gmi/<int:woj_id>', views.showGmina, name='show_gmi'),
    path('create-gmi/', views.createGmina, name='create_gmi'),
    path('display-gmi/', views.displayGmina, name='display_gmi'),
    path('update-gmi/<int:woj_id>/', views.updateGmina, name='update_gmi'),
]