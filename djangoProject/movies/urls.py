from django.urls import path
from . import views
from .views import SeriesDetailView, SearchView

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<slug:slug>/', views.MovieDetailView.as_view(), name='movie-detail'),


    path('series/', views.SeriesListView.as_view(), name='series-list'),
    path('series/<int:pk>/', views.SeriesDetailView.as_view(), name='series-detail'),
    path('series/<slug:slug>/', SeriesDetailView.as_view(), name='series-detail'),

    # ... Search URL patterns ...
    path('search/', SearchView.as_view(), name='search-results'),

    path('genres/<int:pk>/', views.GenreMoviesSeriesView.as_view(), name='genre-movies-series'),
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', views.GenreMoviesSeriesView.as_view(), name='genre_movies_series'),
    # Other URL patterns
]
