from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='rickandmortyapp-home'),
    path('episode/<int:id>/', views.episode, name = 'rickandmortyapp-episode'),
    path('character/<int:id>/', views.character, name = 'rickandmortyapp-character'),
    path('location/<str:name>', views.location, name = 'rickandmortyapp-location'),
    path('search/', views.search, name = 'rickandmortyapp-search'),
    path('locations/', views.locations, name = 'rickandmortyapp-locations'),
    path('characters/', views.characters, name = 'rickandmortyapp-characters')
]
