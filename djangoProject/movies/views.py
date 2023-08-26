
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Movie, Series, Genre
from itertools import zip_longest


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'  # Create this template
    context_object_name = 'movie_list'
    queryset = Movie.objects.order_by('-release_date')  # Order movies by release date descending
    paginate_by = 9


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()  # Get the current movie instance
        featured_movies = Movie.objects.filter(is_featured=True).exclude(id=movie.id)[:9]
        chunks = [featured_movies[i:i+3] for i in range(0, len(featured_movies), 3)]
        context['carousel_chunks'] = chunks
        return context

class SeriesListView(ListView):
    model = Series
    template_name = 'movies/series_list.html'  # Path to your template
    context_object_name = 'series_list'
    queryset = Series.objects.order_by('-release_date')  # Order movies by release date descending
    paginate_by = 9


class SeriesDetailView(DetailView):
    model = Series
    template_name = 'movies/series_detail.html'  # Path to your template
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_series = Series.objects.exclude(slug=self.kwargs['slug'])

        chunk_size = 3
        related_series_chunks = [related_series[i:i + chunk_size] for i in range(0, len(related_series), chunk_size)]

        context['related_series_chunks'] = related_series_chunks
        return context


# SearchView
class SearchView(View):
    template_name = 'movies/search_results.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')
        movies = Movie.objects.filter(title__icontains=query)
        series = Series.objects.filter(title__icontains=query)
        context = {'query': query, 'movies': movies, 'series': series}
        return render(request, self.template_name, context)



class GenreListView(ListView):
    model = Genre
    template_name = 'movies/genre_list.html'
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'movies/genre_detail.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = self.object
        context['movies'] = genre.movie_set.all()
        context['series'] = genre.series_set.all()
        return context


class GenreMoviesSeriesView(View):
    template_name = 'movies/genre_movies_series.html'

    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        movies = Movie.objects.filter(genres=genre)
        series = Series.objects.filter(genres=genre)

        context = {
            'genre': genre,
            'movies': movies,
            'series': series,
        }
        return render(request, self.template_name, context)
