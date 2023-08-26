from django.db import models
from django.urls import reverse
from django.utils.text import slugify



# Genre.
class Genre(models.Model):
     name = models.CharField(max_length=100)
     slug = models.SlugField(unique=True,default='')

     def save(self, *args, **kwargs):
         if not self.slug:
             self.slug = slugify(self.name)
         super().save(*args, **kwargs)

     def __str__(self):
         return self.name


class Movie(models.Model):
     title = models.CharField(max_length=200)
     description = models.TextField(blank=True, null=True)
     release_date = models.DateField(blank=True, null=True)
     is_featured = models.BooleanField(default=False)
     genres = models.ManyToManyField(Genre)
     thumbnail_url = models.URLField(blank=True, null=True)
     trailer_url = models.URLField(blank=True, null=True)
     video_url = models.URLField(blank=True, null=True)
     slug = models.SlugField(unique=True, blank=True)

     def save(self, *args, **kwargs):
         if not self.slug:
             self.slug = slugify(self.title)
         super().save(*args, **kwargs)

     def __str__(self):
         return self.title


# Series model
class Series(models.Model):
     title = models.CharField(max_length=200)
     description = models.TextField(blank=True, null=True)
     release_date = models.DateField(blank=True, null=True)
     is_featured = models.BooleanField(default=False)
     genres = models.ManyToManyField(Genre)
     thumbnail_url = models.URLField(blank=True, null=True)
     trailer_url = models.URLField(blank=True, null=True)
     slug = models.SlugField(unique=True) # Add slug field for URLs

     def __str__(self):
         return self.title

     def get_absolute_url(self):
         return reverse('series-detail', args=[str(self.slug)])


class Season(models.Model):
     series = models.ForeignKey(Series, on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     release_date = models.DateField(blank=True, null=True)
     thumbnail_url = models.URLField(blank=True, null=True)

     def __str__(self):
         return f"{self.series.title} - {self.title}"


class Episode(models.Model):
     season = models.ForeignKey(Season, on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     release_date = models.DateField(blank=True, null=True)
     video_url = models.URLField(blank=True, null=True)

     def __str__(self):
         return f"{self.season.series.title} - {self.season.title} - {self.title}"
