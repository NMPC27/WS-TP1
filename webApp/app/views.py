from django.shortcuts import render
#import file DBquery
from app.DBquery import *

def index(request):

    shows= select_all_12()
    movies= select_all_movies_12()
    tvshows= select_all_TVshow_12()

    args ={
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
        'shows': shows
    }

    return render(requests, 'catalog1.html',args)

def tvshows(requests):
    return render(requests, 'catalog1.html')

def about(requests):
    return render(requests, 'about.html')


