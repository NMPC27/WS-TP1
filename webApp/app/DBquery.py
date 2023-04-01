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

def select_all_12():
    query = """
        PREFIX mov:<http://netflixUA.org/>

        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add ?director_name
        WHERE {
            ?title_id mov:title ?title .
            ?title_id mov:type ?type .
            ?title_id mov:rating ?rating .
            ?title_id mov:director ?director .
            ?director mov:name ?director_name .
            OPTIONAL { ?title_id mov:img ?img }
            ?title_id mov:listed_in ?listed_in .
            ?listed_in mov:name ?genre .
            ?title_id mov:country ?countrys .
            ?countrys mov:name ?country .
            ?title_id mov:description ?desc .
            ?title_id mov:release_year ?release_year .
            ?title_id mov:date_added ?date_add
        }
        GROUP BY ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add ?director_name
        ORDER BY RAND()
        LIMIT 12
    """
    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    # print (res)
    res = res['results']['bindings']
    for e in res:
        e['title_id']['value'] = e['title_id']['value'].split('/')[-1]
    return res


    
def select_all_movies_12():

    query = """
        PREFIX mov:<http://netflixUA.org/>

        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add
        WHERE {
            ?title_id mov:title ?title .
            ?title_id mov:type 'Movie' .
            ?title_id mov:rating ?rating .
            OPTIONAL { ?title_id mov:img ?img }
            ?title_id mov:listed_in ?listed_in .
            ?listed_in mov:name ?genre .
            ?title_id mov:country ?countrys .
            ?countrys mov:name ?country .
            ?title_id mov:description ?desc .
            ?title_id mov:release_year ?release_year .
            ?title_id mov:date_added ?date_add
        }
        GROUP BY ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add
        ORDER BY RAND()
        LIMIT 12
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    # for e in res['results']['bindings']:
    #     print(e['title_id']['value'])
    #     print(e['title']['value'])
    #     print("Movie")
    #     print(e['img']['value'])
    #     print("-----------------")

    res = res['results']['bindings']
    for e in res:
        e['title_id']['value'] = e['title_id']['value'].split('/')[-1]
    return res

def select_all_TVshow_12():

    query = """
        PREFIX mov:<http://netflixUA.org/>

        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add
        WHERE {
            ?title_id mov:title ?title .
            ?title_id mov:type 'TV Show' .
            ?title_id mov:rating ?rating .
            OPTIONAL { ?title_id mov:img ?img }
            ?title_id mov:listed_in ?listed_in .
            ?listed_in mov:name ?genre .
            ?title_id mov:country ?countrys .
            ?countrys mov:name ?country .
            ?title_id mov:description ?desc .
            ?title_id mov:release_year ?release_year .
            ?title_id mov:date_added ?date_add
        }
        GROUP BY ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add
        ORDER BY RAND()
        LIMIT 12
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    # for e in res['results']['bindings']:
    #     print(e['title_id']['value'])
    #     print(e['title']['value'])
    #     print("TV Show")
    #     print(e['img']['value'])
    #     print("-----------------")

    res = res['results']['bindings']
    for e in res:
        e['title_id']['value'] = e['title_id']['value'].split('/')[-1]
    return res

def get_showById(id):

    query = """
        PREFIX mov:<http://netflixUA.org/>
        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add ?director_name

        where { 
            <http://netflixUA.org/show/"""+id+"""> mov:title ?title .
            <http://netflixUA.org/show/"""+id+"""> mov:director ?director .
            ?director mov:name ?director_name .
            <http://netflixUA.org/show/"""+id+"""> mov:type ?type  .
            <http://netflixUA.org/show/"""+id+"""> mov:img ?img .
            <http://netflixUA.org/show/"""+id+"""> mov:title ?title .
            <http://netflixUA.org/show/"""+id+"""> mov:listed_in ?listed_in .
            ?listed_in mov:name ?genre .
            <http://netflixUA.org/show/"""+id+"""> mov:country ?countrys .
            ?countrys mov:name ?country .
            <http://netflixUA.org/show/"""+id+"""> mov:description ?desc .
            <http://netflixUA.org/show/"""+id+"""> mov:release_year ?release_year .
            <http://netflixUA.org/show/"""+id+"""> mov:date_added ?date_add .
    }    
    group by ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add ?director_name 
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    
    # for e in res['results']['bindings']:
    #     print(e['title_id']['value'])
    #     print(name)
    #     print(e['type']['value'])
    #     print(e['img']['value'])
    #     print("-----------------")
    return res['results']['bindings']



def select_search(name):
    query = """
        PREFIX mov:<http://netflixUA.org/>
        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add
        WHERE{
            ?title_id mov:title '"""+name+"""' .
            ?title_id mov:type ?type  .
            ?title_id mov:img ?img .
            ?title_id mov:title ?title .
            ?title_id mov:listed_in ?listed_in .
            ?listed_in mov:name ?genre .
            ?title_id mov:country ?countrys .
            ?countrys mov:name ?country .
            ?title_id mov:description ?desc .
            ?title_id mov:release_year ?release_year .
            ?title_id mov:date_added ?date_add
        }
        GROUP BY ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add
        
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    
    # for e in res['results']['bindings']:
    #     print(e['title_id']['value'])
    #     print(name)
    #     print(e['type']['value'])
    #     print(e['img']['value'])
    #     print("-----------------")
    return res['results']['bindings']
        
# select_search("King Jack")


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



