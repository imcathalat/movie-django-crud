from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from movies_uploads.models import Movie
from movies_uploads.forms import UploadForm #instanciando um formulario de forms.py


def home(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/home.html', context)

def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        context = {
            'movie': movie
        }
        return render(request, 'movies/movie.html', context)
    else:
        raise Http404('Movie does not exist')

def upload(request):
    if request.POST:    
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return (home)
    else:
        form = UploadForm()
    return render(request, 'movies/upload.html', {'form': form})


# Se eu fosse fazer com DetailView (maneira mais facil) ficaria da seguinte forma:
# 1) Fazer alguns imports:
    # from django.views import generic
# 2) Fazer classe da DetailView:
    # class ClassDetailView(generic.DetailView):
        # model = Model
        # template_name = 'pasta/template.html'
        # queryset = Model.objects.all()
        # context_object_name = 'contatex_name'