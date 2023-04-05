from django.shortcuts import render
#import file DBquery
from app.DBquery import *
from pprint import pprint
#from jinja2 import Environment, FileSystemLoader

def index(request):

    shows= select_all_12()
    movies= select_all_movies_12()
    tvshows= select_all_TVshow_12()

    args = {
        'shows': shows,
        'movies': movies,
        'tvshows': tvshows,
    }


    return render(request, 'index.html',args)

def details(requests, id): # str id

    
    # dic = select_search(requests.GET['show'])
    dic = get_showById(id)
    #pass dic to dictionary
    dic = {'dic': dic[0]}
    pprint(dic)

    
    return render(requests, 'details1.html', dic)

def movies(requests,page):
    shows= select_all_12()

    args = {
        'shows': shows,
        'movies': 1,
        'page':page
    }

    return render(requests, 'catalog1.html',args)

def tvshows(requests,page):
    shows= select_all_TVshow_12()

    args = {
        'shows': shows,
        'movies': 0,
        'page':page
    }

    return render(requests, 'catalog1.html',args)

def search(requests): # pesquisa por pessoas e nomes de filmes/series
    shows= select_all_TVshow_12()

    
    if len(requests.GET.keys())!=0:
        #this is a searchç
        
        print(requests.GET)
        queryargs = {k:requests.GET[k] for k in requests.GET.keys() if requests.GET[k]!="All" and requests.GET[k]!=""}
        queryargs['limit'] = 12
        shows= searchQuery(queryargs)
        args = {
            'shows': shows,
            "search_query": requests.GET['search_query'] if requests.GET.get('search_query') else "All",
            'filter_genre': requests.GET.get('genre') if requests.GET.get('genre') else "All",
            "filter_year": requests.GET.get('release_year') if requests.GET.get('release_year') else "All",
            "filter_country": requests.GET.get('country') if requests.GET.get('country') else "All",
            "rating": requests.GET.get('rating') if requests.GET.get('rating') else "All",
            'type': "All",
            'page': requests.GET.get('page') if requests.GET.get('rating') else "1"
        }

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

def insert(requests):
    return render(requests, 'insert.html')

def test_site(requests):
    return render(requests, 'test_site.html')

def not_found(request):
    return render(request, '404.html')