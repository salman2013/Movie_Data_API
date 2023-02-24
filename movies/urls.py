from django.urls import path
from movies.views import MovieListView

app_name = 'movies'

urlpatterns = [
    path('movies_list/', MovieListView.as_view()),
]
