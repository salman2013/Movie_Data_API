from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    image = models.URLField(max_length=200, null=True)
    heath = models.URLField(null=True)
    url = models.URLField(null=True)
    type = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True)
    image_urls = models.JSONField(null=True)
