from django.shortcuts import render
#import file DBquery
from app.DBquery import *
from jinja2 import Environment, FileSystemLoader

def not_found(request, exception):
    return render(request, '404.html', status=404)

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

    
    return render(requests, 'details1.html', dic)

def movies(requests):

    shows= select_all_movies_12()

    args ={
        'movies': 1,
        'shows': shows
    }

    return render(requests, 'catalog1.html',args)

def tvshows(requests):
    shows= select_all_TVshow_12()

    args ={
        'movies': 0,
        'shows': shows
    }

    return render(requests, 'catalog1.html',args)

def filter(requests):

    if requests.method == 'GET': ## para aparecer no url
        print(requests.GET['filter_genre'], requests.GET['filter_year'], requests.GET['filter_country'], requests.GET['filter_rate'])

    shows= select_all_12()

    args = {
        'shows': shows,
        'filter_genre': "ola",
        'filter_year': 2727,
        'filter_country': "pp",
        'filter_rate': "0-1",
    }


    return render(requests, 'catalog_filter.html',args)

def about(requests):
    return render(requests, 'about.html')

def insert(requests):
    return render(requests, 'insert.html')

def not_found(request):
    return render(request, '404.html')