from django.shortcuts import render
from rest_framework import generics
from movies.models import Movie
from movies.serializer import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend


class MovieListView(generics.ListAPIView):

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['movie_id', 'name', 'type', 'year']
