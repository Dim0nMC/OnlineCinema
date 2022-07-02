from django.shortcuts import render
from app.movies.models import Movie


def index_page(request):
    movies = Movie.object.all()
    return render(request, 'movies/index.html', {'movies': movies})

def player_page(request, id):
    return render(request, 'movies/player.htmlm', {'id': id})
