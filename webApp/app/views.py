from django.shortcuts import render
#import file DBquery
from app.DBquery import *
from app.utils import *
from django.views.decorators.csrf import csrf_exempt

def index(request: object):

    shows= select_all_12()
    movies= select_all_movies_12(1)
    tvshows= select_all_TVshow_12(1)

    args = {
        'shows': shows,
        'movies': movies,
        'tvshows': tvshows,
    }


    return render(request, 'index.html',args)

def details(requests, id: str):

    
    # dic = select_search(requests.GET['show'])
    dic = get_showById(id)
    #pass dic to dictionary
    dic = {'dic': dic[0]}
    
    return render(requests, 'details.html', dic)

def movies(requests,page):
    shows= select_all_movies_12(page)

    args = {
        'shows': shows,
        'type': "Movies",
        'page':page
    }

    return render(requests, 'catalog1.html',args)

def tvshows(requests,page: str):
    shows= select_all_TVshow_12(page)

    args = {
        'shows': shows,
        'type': "Tv Shows",
        'page':page
    }

    return render(requests, 'catalog1.html',args)

def search(requests): # pesquisa por pessoas e nomes de filmes/series
    shows= select_all_12()

    
    if len(requests.GET.keys())!=0:
        #this is a searchç
        
        searchArgs = validate_request(requests.GET)
        print(searchArgs)
        
        
        queryargs = {k:searchArgs[k] for k in searchArgs.keys() if searchArgs[k]!="All" and searchArgs[k]!=""}
        queryargs['limit'] = 12
        shows= searchQuery(queryargs)
        args = {
            'shows': shows,
            "search_query": searchArgs.get('query') if searchArgs.get('query') else "All",
            'filter_genre': searchArgs.get('genre') if searchArgs.get('genre') else "All",
            "filter_year": searchArgs.get('release_year') if searchArgs.get('release_year') else "All",
            "filter_country": searchArgs.get('country') if searchArgs.get('country') else "All",
            "rating": searchArgs.get('rating') if searchArgs.get('rating') else "All",
            'type': searchArgs.get('type') if searchArgs.get('type') else "All",
            'page': searchArgs.get('page') if searchArgs.get('page') else "1"
            
        }

        #only limit and one thing
        if len(queryargs) == 2:
            args["search"]= searchArgs[list(searchArgs.keys())[0]]
        
        else:
            string_gen = (queryargs[x] for x in queryargs.keys() if x!="limit" and x!="page")
            #comma between each element, except last
            args["search"] = ", ".join(string_gen)
                

        #query
        return render(requests, 'search.html',args)
    #this is not a search
    args = {
        'shows': select_all_12(),
        'search_query': "",
        'filter_genre': "All",
        'filter_year': "All",
        'filter_country': "All" ,
        'rating': "All",
        'type': "All",
        'page': "1"
    }
    
    return render(requests, 'search.html', args)

def about(requests):
    return render(requests, 'about.html')

@csrf_exempt
def insert(requests):

    if len(requests.POST.keys())!=0:
        if requests.POST["action"] == "insert" and requests.POST["insert-input-title"] != "":
            print("insert")
            print(requests.POST)
        #    def insertData(title, type=None, rating=None, director=None, img=None, listed_in=None, country=None, description=None, release_year=None, date_added=None, cast=None,trailer=None):
            title = requests.POST["insert-input-title"]
            type = requests.POST["insert-input-type"]
            rating = requests.POST["insert-input-rating"]
            director = requests.POST["insert-input-director_name"].strip().split(",")
            img = requests.POST["insert-input-img"]
            listed_in = requests.POST["insert-input-genres"].strip().split(",")
            country = requests.POST["insert-input-countries"].strip().split(",")
            description = requests.POST["insert-input-desc"]
            release_year = requests.POST["insert-input-release_year"]
            date_added = requests.POST["insert-input-date_add"]
            cast = requests.POST["insert-input-cast"].strip().split(",")
            trailer = requests.POST["insert-input-trailer"]
            if title == "":
                title = None
            if type == "":
                type = None
            if rating == "":
                rating = None
            if director[0] == "":
                director = None
            if img == "":
                img = None
            if listed_in[0] == "":
                listed_in = None
            if country[0] == "":
                country = None
            if description == "":
                description = None
            if release_year == "":
                release_year = None
            if date_added == "":
                date_added = None
            if cast[0] == "":
                cast = None
            if trailer == "":
                trailer = None
    
            insertData(title,type=type, rating=rating, director=director, img=img, listed_in=listed_in, country=country, description=description, release_year=release_year, date_added=date_added, cast=cast,trailer=trailer)
                
            
        elif requests.POST["action"] == "remove" and requests.POST["remove-input"] != "":
            deleteByTitle(requests.POST["remove-input"])
            
        elif requests.POST["action"] == "edit" and requests.POST["edit-input-title"] != "":
            print("edit")
            print(requests.POST["edit-input-title"])

    return render(requests, 'insert.html')

def test_site(requests):
    return render(requests, 'test_site.html')

def not_found(request):
    return render(request, '404.html')