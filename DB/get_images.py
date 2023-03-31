import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient
import requests


endpoint = "http://localhost:7200"
repo_name = "movies" #! change this to your repository name

client = ApiClient(endpoint=endpoint)
accessor = GraphDBApi(client)

theMovie_api_key = "c08d35426ff385e63e4b2657a12bafea"

def select_all_movies():
    f = open("movies_img.csv", "a")

    query = """
        PREFIX mov:<http://netflixUA.org/>
        SELECT ?title ?title_id
        WHERE{
            ?title_id mov:title ?title .
            ?title_id mov:type 'Movie' .
        }
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    for e in res['results']['bindings']:
        print(e['title_id']['value'])

        try:
            img=get_img(e['title']['value'])
            f.write('<'+e['title_id']['value']+'> <http://netflixUA.org/img> "'+img+'" .\n')
        except:
            f.write('<'+e['title_id']['value']+'> <http://netflixUA.org/img> "NO_IMAGE" .\n')

    f.close()

def select_all_TVshow():
    f = open("TVshow_img.csv", "a")

    query = """
        PREFIX mov:<http://netflixUA.org/>
        SELECT ?title ?type ?title_id
        WHERE{
            ?title_id mov:title ?title .
            ?title_id mov:type 'TV Show' .
        }
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    for e in res['results']['bindings']:
        print(e['title_id']['value'])

        try:
            img=get_img(e['title']['value'])
            f.write('<'+e['title_id']['value']+'> <http://netflixUA.org/img> "'+img+'" .\n')
        except:
            f.write('<'+e['title_id']['value']+'> <http://netflixUA.org/img> "NO_IMAGE" .\n')
            

    f.close()


def get_img(name):
    url = "https://api.themoviedb.org/3/search/movie?api_key="+theMovie_api_key+"&query="+name
    response = requests.get(url)
    dict_values = json.loads(response.text)

    movie_id=dict_values['results'][0]['id']

    url = "https://api.themoviedb.org/3/movie/"+str(movie_id)+"/images?api_key="+theMovie_api_key
    response = requests.get(url)
    dict_values = json.loads(response.text)

    return "https://image.tmdb.org/t/p/w500"+dict_values['posters'][0]['file_path']

def get_img2(name):
    url = "https://api.themoviedb.org/3/search/tv?api_key="+theMovie_api_key+"&query="+name
    response = requests.get(url)
    dict_values = json.loads(response.text)

    movie_id=dict_values['results'][0]['id']

    url = "https://api.themoviedb.org/3/tv/"+str(movie_id)+"/images?api_key="+theMovie_api_key
    response = requests.get(url)
    dict_values = json.loads(response.text)

    return "https://image.tmdb.org/t/p/w500"+dict_values['posters'][0]['file_path']

select_all_movies()
select_all_TVshow()