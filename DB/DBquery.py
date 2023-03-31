import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient


endpoint = "http://localhost:7200"
repo_name = "movies" #! change this to your repository name

client = ApiClient(endpoint=endpoint)
accessor = GraphDBApi(client)


# select_all()
# select_all_movies()
# select_all_TVshow()
# select_search("King Jack")

def select_all():

    query = """
        PREFIX mov:<http://netflixUA.org/>
        SELECT ?title ?type ?title_id ?img  
        WHERE{
            ?title_id mov:title ?title .
            ?title_id mov:type ?type .
            ?title_id mov:img ?img .
        }
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    for e in res['results']['bindings']:
        print(e['title_id']['value'])
        print(e['title']['value'])
        print(e['type']['value'])
        print(e['img']['value'])
        print("-----------------")


    
def select_all_movies():

    query = """
        PREFIX mov:<http://netflixUA.org/>
        SELECT ?title ?title_id ?img
        WHERE{
            ?title_id mov:title ?title .
            ?title_id mov:type 'Movie' .
            ?title_id mov:img ?img .
        }
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    for e in res['results']['bindings']:
        print(e['title_id']['value'])
        print(e['title']['value'])
        print("Movie")
        print(e['img']['value'])
        print("-----------------")

def select_all_TVshow():

    query = """
        PREFIX mov:<http://netflixUA.org/>
        SELECT ?title ?title_id ?img
        WHERE{
            ?title_id mov:title ?title .
            ?title_id mov:type 'TV Show' .
            ?title_id mov:img ?img .
        }
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    for e in res['results']['bindings']:
        print(e['title_id']['value'])
        print(e['title']['value'])
        print("TV Show")
        print(e['img']['value'])
        print("-----------------")


def select_search(name):
    query = """
        PREFIX mov:<http://netflixUA.org/>
        SELECT ?type ?title_id ?img
        WHERE{
            ?title_id mov:title '"""+name+"""' .
            ?title_id mov:type ?type  .
            ?title_id mov:img ?img .
        }
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    for e in res['results']['bindings']:
        print(e['title_id']['value'])
        print(name)
        print(e['type']['value'])
        print(e['img']['value'])
        print("-----------------")


########################################################################

# def select():

#     query = """
#         PREFIX mov:<http://netflixUA.org/>
#         SELECT ?title ?type 
#         WHERE{
#             ?pessoa_id mov:name "Julien Leclercq" .
#             ?title_id mov:director ?pessoa_id .
#             ?title_id mov:title ?title .
#             ?title_id mov:type ?type .
#         }
#     """

    

#     payload_query = {"query": query}
#     res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
#     res = json.loads(res)
#     for e in res['results']['bindings']:
#         print(e['title']['value'],e['type']['value'])


# def insert():
#     update = """
#     PREFIX mov:<http://movies.org/pred/>
#     PREFIX move: <http://movies.org/>
#     INSERT DATA
#     {
#         move:my_life mov:name "My Life in Hell" .
#     }
#     """

#     payload_query = {"update": update}
#     res = accessor.sparql_update(body=payload_query,repo_name=repo_name)


# def delete():
#     update = """
#     PREFIX mov:<http://movies.org/pred/>
#     PREFIX move: <http://movies.org/>
#     DELETE DATA
#     {
#         move:my_life mov:name "My Life in Hell" .
#     }
#     """
#     payload_query = {"update": update}
#     res = accessor.sparql_update(body=payload_query,repo_name=repo_name)



