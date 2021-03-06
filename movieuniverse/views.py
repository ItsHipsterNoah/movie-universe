from django.shortcuts import get_object_or_404, redirect, render
from .models import Movie
from sklearn.neighbors import NearestNeighbors
import django_pandas.io as djpd
from titlecase import titlecase
from django.core.paginator import Paginator


def index(request):
    if 'recommendations' in request.session:
        recent_search = request.session['recommendations'][6:]
    else:
        recent_search = []
    results = Movie.objects.filter(id__in=recent_search)
    return render(request, 'movieuniverse/index.html', {
        'results' : results
    })





def result(request):
    search_query = request.GET.get('search').strip()
    netflix = request.GET.get('netflix')
    hulu = request.GET.get('hulu')
    disney = request.GET.get('disney')
    prime = request.GET.get('prime')
    recommended_movies = ''
    recommendations = []
    more_movies = []
    if search_query:
        if "," in search_query:
            search_query = search_query.split(', ')
            search_query = [word.capitalize() for word in search_query]
            search_query = ', '.join(search_query) 
        results = Movie.objects.filter(title__contains=titlecase(search_query)) | Movie.objects.filter(title__exact=titlecase(search_query))
        results = results | Movie.objects.filter(directors__contains=titlecase(search_query)) | Movie.objects.filter(directors__exact=titlecase(search_query))
        results = results | Movie.objects.filter(genres__contains=titlecase(search_query)) | Movie.objects.filter(genres__exact=titlecase(search_query))
        if netflix == 'on':
            results = results.filter(netflix__exact=1)
        elif hulu == 'on':
            results = results.filter(hulu__exact=1)
        elif disney == 'on':
            results = results.filter(disney__exact=1)
        elif prime == 'on':
            results = results.filter(prime__exact=1)
        if results:
            for result in results:
                df = djpd.read_frame(Movie.objects.all().defer('title', 'age', 'directors', 'genres', 'country', 'language', 'runtime'))
                X = df[['year', 'IMDb_rating', 'Rotten_Tomatoes_rating']].dropna().values
                nbrs = NearestNeighbors(n_neighbors=10).fit(X)
                recommended_movies = nbrs.kneighbors([[result.year, result.IMDb_rating, result.Rotten_Tomatoes_rating]])[1]
                for r_movie in recommended_movies[:6]: 
                    recommendations.extend(df.iloc[r_movie-1]['title'].values.tolist())
                request.session['recommendations'] = recommended_movies.tolist()[0]
                request.session.modified = True
            more_movies = Movie.objects.filter(genres__exact=results[0].genres).order_by('?')[:3]
            paginator = Paginator(results, 6)
            page_number = request.GET.get('page')
            paginated_movies = paginator.get_page(page_number)
            return render(request, 'movieuniverse/results.html', { 
                "query" : search_query,
                "movies" : paginated_movies,
                "recommendations" : recommendations[:6],
                "more_movies" : more_movies,
                "netflix" : netflix,
                "hulu" : hulu,
                "disney" : disney,
                "prime" : prime
            })
        else:
            return  render(request, 'movieuniverse/results.html', {
                "query" : search_query,
            })
    else:
        return  render(request, 'movieuniverse/results.html', {
                "query" : search_query,
            })

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movieuniverse/detail.html', { 'movie': movie })

def recommendation_detail(request, title):
    movie_id = Movie.objects.get(title__exact=title).id
    return redirect(f'/movie/{movie_id}')

def stats(request):
    return render(request, 'movieuniverse/insights.html')

def handle404(request, exception):
    return render(request, 'movieuniverse/404.html', status=404)
