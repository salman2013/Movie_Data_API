from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'name', 'language',
                  'image', 'url', 'heath', 'type', 'description', 'image_urls', 'year']
