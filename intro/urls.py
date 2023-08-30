from django.urls import path

from intro import views

urlpatterns = [
    path('first_page/',views.hello, name='first-page'),
    path('show_name/',views.name, name='show-page'),
    path('list_of_cars/', views.cars, name='list-of-cars'),
    path('list_of_movies/', views.movies, name='list-of-movies')
]

# Prefixul este unic
# Name este unic
# Fiecare path va avea o functie/clasa