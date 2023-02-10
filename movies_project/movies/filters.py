from rest_framework import filters
from .models import Movie


class SearchByMovieIDFilter(filters.BaseFilterBackend):
    """
        Filter to search movie by id.
    """

    def filter_queryset(self, request, queryset, view):
        id = request.GET.get('movie_id', '')
        if id is not None:
            return queryset.filter(movie_id=id)
        else:
            movie_name = request.GET.get('name', '')
            if movie_name is not None:
                return queryset.filter(name=movie_name)
            else:
                movie_type = request.GET.get('type', '')
                return queryset.filter(type=movie_type)


class SearchByMovieNameFilter(filters.BaseFilterBackend):
    """
        Filter to search movie by name.
    """

    def filter_queryset(self, request, queryset, view):
        movie_name = request.GET.get('name', '')
        print("name " + movie_name)
        return queryset.filter(name=movie_name)


class SearchByMovieTypeFilter(filters.BaseFilterBackend):
    """
        Filter to search movie by name.
    """

    def filter_queryset(self, request, queryset, view):
        movie_type = request.GET.get('type', '')
        print("name " + movie_type)
        return queryset.filter(type=movie_type)
