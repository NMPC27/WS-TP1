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
            'page': searchArgs.get('page') if searchArgs.get('page') else "1",
            'order_by': searchArgs.get('order_by') if searchArgs.get('order_by') else "Off",

        }

        #only limit and one thing
        if len(queryargs) == 2:
            args["search"]= searchArgs[list(searchArgs.keys())[0]]

        else:
            string_gen = (queryargs[x] for x in queryargs.keys() if x!="limit" and x!="page" and x!="order_by")
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
        'order_by': "Off",
        'page': "1",
    }

    return render(requests, 'search.html', args)

def about(requests):
    return render(requests, 'about.html')

@csrf_exempt
def insert(requests):

    show_data_div = False
    show_insert_div = False
    show_remove_div = False
    newid = None
    success_insert = "None"
    success_get_edit = "None"
    success_remove = "None"

    edit_data = None



    if len(requests.POST.keys())!=0:
        if requests.POST["action"] == "insert" :
            show_insert_div = True
            if requests.POST["insert-input-title"] != "":
            #    def insertData(title, type=None, rating=None, director=None, img=None, listed_in=None, country=None, description=None, release_year=None, date_added=None, cast=None,trailer=None):
                title = requests.POST["insert-input-title"]
                type = "Movie" if requests.POST["insert-input-type"].strip().lower() == "movie" else "TV Show"
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
                    img = "NO_IMAGE"
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

                newid = insertData(title,type=type, rating=rating, director=director, img=img, listed_in=listed_in, country=country, description=description, release_year=release_year, date_added=date_added, cast=cast,trailer=trailer)
                if int(newid) != -1:
                    success_insert = "True"
                else:
                    success_insert = "False"
            else:
                success_insert = "False"

        elif requests.POST["action"] == "remove" :
            show_remove_div = True
            if requests.POST["remove-input"] != "":
                res = deleteByTitle(requests.POST["remove-input"])
                success_remove = "True"
            else:
                success_remove = "False"

        elif requests.POST["action"] == "edit-get" :
            show_data_div = True
            if requests.POST["id"] != "none" and requests.POST["id"] != "":
                title = getTitleById(requests.POST["id"])
                if len(title) >=1:
                    title = title[0]["title"]["value"]
                show = get_showById(requests.POST["id"])
                if len(show) >=1:
                    show = show[0]
                    type = requests.POST["data-div-type"].strip()
                    rating = requests.POST["data-div-rating"].strip()
                    director = requests.POST["data-div-director"].strip().split(",")
                    img = requests.POST["data-div-image"].strip()
                    listed_in = requests.POST["data-div-genres"].strip().split(",")
                    country = requests.POST["data-div-countries"].strip().split(",")
                    description = requests.POST["data-div-desc"].strip()
                    release_year = requests.POST["data-div-rel_year"].strip()
                    date_added = requests.POST["data-div-added_date"].strip()
                    cast = requests.POST["data-div-cast"].strip().split(",")
                    trailer = requests.POST["data-div-trailer"].strip()
                        
                    if title != "":
                        if type == "":
                            type = "UNKNOWN"
                        if rating == "":
                            rating = "N/A"
                        if director == "":
                            director = "UNKNOWN"
                        if img == "":
                            img = "NO_IMAGE"
                        if listed_in == "":
                            listed_in = "UNKNOWN"
                        if country == "":
                            country = "UNKNOWN"
                        if description == "":
                            description = "UNKNOWN"
                        if release_year == "":
                            release_year = "UNKNOWN"
                        if date_added == "":
                            date_added = "UNKNOWN"
                        if cast == "":
                            cast = "UNKNOWN"
                        if trailer == "":
                            trailer = "UNKNOWN"
                        deleteByTitle(title)
                        newid = insertData(title, type=type, rating=rating, director=director, img=img, listed_in=listed_in, country=country, description=description, release_year=release_year, date_added=date_added, cast=cast,trailer=trailer,title_id=requests.POST["id"].replace("s",""))

            if requests.POST["data-div-title"] != "":
                dic ={}
                dic["query"] = requests.POST["data-div-title"]
                edit_data = select_search(requests.POST["data-div-title"])
                #if edit_data has length bigger than 1
                if len(edit_data) >= 1:
                    edit_data = edit_data[0]
                    success_get_edit = "True"
                else:
                    success_get_edit = "False"
            else:
                success_get_edit = "False"


    args = {"show_data_div": show_data_div , "success_get_edit": success_get_edit, "success_insert": success_insert, "success_remove": success_remove, "show_insert_div": show_insert_div, "show_remove_div": show_remove_div,
            "edit_data" : edit_data
            }
    if len(requests.POST.keys())!=0:
        if requests.POST["action"] == "edit-get" or requests.POST["action"] == "insert":
            args["newid"] = newid
    return render(requests, 'insert.html', args)

def test_site(requests):
    return render(requests, 'test_site.html')

def not_found(request):
    return render(request, '404.html')