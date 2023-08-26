from django.contrib import admin
from django.utils.html import format_html

from .models import Genre, Movie, Series, Season, Episode



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'is_featured', 'display_thumbnail')
    list_filter = ('is_featured', 'genres')
    prepopulated_fields = {'slug': ('title',)}

    def display_thumbnail(self, obj):
        return format_html('<img src="{}" width="80" height="50">', obj.thumbnail_url)
    display_thumbnail.short_description = 'Thumbnail'


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1

class SeasonInline(admin.TabularInline):
    model = Season
    extra = 1


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'is_featured', 'display_thumbnail')
    list_filter = ('is_featured', 'genres')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SeasonInline]

    def display_thumbnail(self, obj):
        return format_html('<img src="{}" width="80" height="50">', obj.thumbnail_url)
    display_thumbnail.short_description = 'Thumbnail'


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('title', 'series', 'release_date')
    list_filter = ('series',)
    inlines = [EpisodeInline]


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'season', 'release_date')
    list_filter = ('season__series', 'season')
    ordering = ('season__series', 'season__title', 'title')  # Order by series and season title





