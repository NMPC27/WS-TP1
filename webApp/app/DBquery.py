import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient


endpoint = "http://localhost:7200"
repo_name = "movies" #! change this to your repository name

client = ApiClient(endpoint=endpoint)
accessor = GraphDBApi(client)


def select_all_12():
    query = """
        PREFIX mov:<http://netflixUA.org/>

        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add (GROUP_CONCAT(DISTINCT ?director_name; SEPARATOR=", ") as ?directors)  (GROUP_CONCAT(DISTINCT ?cast_person; SEPARATOR=", ") as ?cast) 
        WHERE {
            ?title_id mov:title ?title .
            OPTIONAL {?title_id mov:rating ?rating }
            OPTIONAL {?title_id mov:director ?director .
                ?director mov:name ?director_name .}
            OPTIONAL {
				?title_id mov:listed_in ?listed_in .
                ?listed_in mov:name ?genre .
            }
    		OPTIONAL{?title_id mov:type ?type .
            ?title_id mov:img ?img .
            ?title_id mov:country ?countrys .
            ?countrys mov:name ?country .
            ?title_id mov:description ?desc .
            ?title_id mov:release_year ?release_year .
            ?title_id mov:date_added ?date_add . 
    		?title_id mov:cast ?person .
    		?person mov:name ?cast_person .
    	    }
        }
        GROUP BY ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add 

        ORDER BY Rand()
        LIMIT 12
    """
    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    res = res['results']['bindings']
    for e in res:
        e['title_id']['value'] = e['title_id']['value'].split('/')[-1]
        # if not 'rating' in e:
        #     #insert N/A in rating
        #     e['rating'] = {}
        #     e['rating']['value'] = "N/A"
            
    return res


    
def select_all_movies_12():

    query = """
        PREFIX mov:<http://netflixUA.org/>

        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add (GROUP_CONCAT(DISTINCT ?director_name; SEPARATOR=", ") as ?directors)
        WHERE {
            ?title_id mov:title ?title .
            ?title_id mov:type "Movie" .
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
        GROUP BY ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add 
        ORDER BY Rand()
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

        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add (GROUP_CONCAT(DISTINCT ?director_name; SEPARATOR=", ") as ?directors)
        WHERE {
            ?title_id mov:title ?title .
            ?title_id mov:type "TV Show" .
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
        GROUP BY ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add 
        ORDER BY Rand()
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
        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add (GROUP_CONCAT(DISTINCT ?director_name; SEPARATOR=", ") as ?directors) (GROUP_CONCAT(DISTINCT ?cast_person; SEPARATOR=", ") as ?cast)

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
            <http://netflixUA.org/show/"""+id+"""> mov:cast ?person .
    		?person mov:name ?cast_person .
    }    
    group by ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add 
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
    for e in res['results']['bindings']:
        e['title_id']['value'] = e['title_id']['value'].split('/')[-1]
    return res['results']['bindings']
        
def searchQuery(argsdict):

    query = """
        PREFIX mov:<http://netflixUA.org/>
        
        SELECT DISTINCT ?title ?type ?title_id ?img ?rating (GROUP_CONCAT(DISTINCT ?genre; SEPARATOR=", ") as ?genres) (GROUP_CONCAT(DISTINCT ?country; SEPARATOR=", ") as ?countries) ?desc ?release_year ?date_add (GROUP_CONCAT(DISTINCT ?director_name; SEPARATOR=", ") as ?directors)
        WHERE {
            ?title_id mov:title ?title .
            
            OPTIONAL{?title_id mov:type ?type .
            ?title_id mov:rating ?rating .
            ?title_id mov:director ?director .
            ?director mov:name ?director_name .
            ?title_id mov:img ?img .
            ?title_id mov:listed_in ?listed_in .
            ?listed_in mov:name ?genre .
            ?title_id mov:country ?countrys .
            ?countrys mov:name ?country .
            ?title_id mov:description ?desc .
            ?title_id mov:release_year ?release_year .
            ?title_id mov:date_added ?date_add . 
    		?title_id mov:cast ?person .
    		?person mov:name ?cast_person .
      }
            """
            
    title = argsdict.get('title')
    type = argsdict.get('type')
    genre = argsdict.get('genre')
    country = argsdict.get('country')
    director = argsdict.get('director')
    actor = argsdict.get('actor')
    release_year = argsdict.get('release_year')
    
    if title != None:
        query += "?title_id mov:title \""+title+"\" .\n"
    if type != None:
        query += "?title_id mov:type \""+type+"\" .\n"
    if genre != None:
        query += "?title_id mov:listed_in ?listed_inn .\n"
        query += "?listed_inn mov:name \""+genre+"\" .\n"
    if country != None:
        query += "?title_id mov:country ?countrys .\n"
        query += "?countrys mov:name \""+country+"\" .\n"
    if director != None:
        query += "?title_id mov:director ?director .\n"
        query += "?director mov:name \""+director+"\" .\n"
    if actor != None:
        query += "?title_id mov:cast ?person .\n"
        query += "?person mov:name \""+actor+"\" .\n"
    if release_year != None:
        query += "?title_id mov:release_year \""+release_year+"\" .\n"
    # if date_added != None:
    #     query += "?title_id mov:date_added \""+date_added+"\" .\n"
    query += """
        
        }
        GROUP BY ?title ?type ?title_id ?img ?rating ?desc ?release_year ?date_add 
        """
    limit = argsdict.get('limit')
    if limit != None:
        query += "LIMIT "+str(limit)

    # print(query)
    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    try:
        res = json.loads(res)
    except:
        return []
    for e in res['results']['bindings']:
        e['title_id']['value'] = e['title_id']['value'].split('/')[-1]
    return res['results']['bindings'] 

def getNewTitleId():#!TODO GET A NEW ID FROM DB
    CurrID = 8888
    return str(CurrID+1)

def insertData(title, type=None, rating=None, director=None, img=None, listed_in=None, country=None, description=None, release_year=None, date_added=None, cast=None):
    
    curr_title_id = getNewTitleId()
    
    if type == None:
        type ="UNKNOWN"
    if rating == None:
        rating = "UNKNOWN"
    if img == None:
        img = "UNKNOWN"
    if description == None:
        description = "UNKNOWN"
    if release_year == None:
        release_year = "UNKNOWN"
    if date_added == None:
        date_added = "UNKNOWN"


    query = """
        PREFIX mov:<http://netflixUA.org/>
        PREFIX title:<http://netflixUA.org/show/s>
        PREFIX director: <http://netflixUA.org/director/>
        PREFIX listed_in: <http://netflixUA.org/genre/>
        PREFIX country: <http://netflixUA.org/country/>
        PREFIX person: <http://netflixUA.org/person/>
        INSERT DATA
        {
            title:"""+str(curr_title_id)+""" mov:title '"""+title+"""' .
            title:"""+str(curr_title_id)+""" mov:type '"""+type+"""' .
            title:"""+str(curr_title_id)+""" mov:rating '"""+rating+"""' .
            title:"""+str(curr_title_id)+""" mov:img '"""+img+"""' .
            title:"""+str(curr_title_id)+""" mov:description '"""+description+"""' .
            title:"""+str(curr_title_id)+""" mov:release_year '"""+release_year+"""' .
            title:"""+str(curr_title_id)+""" mov:date_added '"""+date_added+"""' .
    """
    if director == None:
        director = "UNKNOWN"
        director_uri = "person:"+director.lower().replace(" ", "_")
        query += " title:"+str(curr_title_id)+" mov:director "+director_uri+" .\n"
        query += director_uri+" mov:name '"+director+"' .\n"
    else:
        for name in director:
            director_uri = "person:"+name.lower().replace(" ", "_")
            query += " title:"+str(curr_title_id)+" mov:director "+director_uri+" .\n"
            query += director_uri+" mov:name '"+name+"' .\n"
    if listed_in == None:
        listed_in = "UNKNOWN"
        listed_in_uri = "listed_in:"+listed_in.lower().replace(" ", "_")
        query += " title:"+str(curr_title_id)+" mov:listed_in "+listed_in_uri+" .\n"
        query += listed_in_uri+" mov:name '"+listed_in+"' .\n"
    else:
        for name in listed_in:
            listed_in_uri = "listed_in:"+name.lower().replace(" ", "_")
            query += " title:"+str(curr_title_id)+" mov:listed_in "+listed_in_uri+" .\n"
            query += listed_in_uri+" mov:name '"+name+"' .\n"
    if country == None:
        country = "UNKNOWN"
        country_uri = "country:"+country.lower().replace(" ", "_")
        query += " title:"+str(curr_title_id)+" mov:country "+country_uri+" .\n"
        query += country_uri+" mov:name '"+country+"' .\n"
    else:
        for name in country:
            country_uri = "country:"+name.lower().replace(" ", "_")
            query += " title:"+str(curr_title_id)+" mov:country "+country_uri+" .\n"
            query += country_uri+" mov:name '"+name+"' .\n"
    if cast == None:
        cast = "UNKNOWN"
        cast_uri = "person:"+cast.lower().replace(" ", "_")
        query += " title:"+str(curr_title_id)+" mov:cast "+cast_uri+" .\n"
        query += cast_uri+" mov:name '"+cast+"' .\n"
    else:
        for name in cast:
            cast_uri = "cast:"+name.lower().replace(" ", "_")
            query += " title:"+str(curr_title_id)+" mov:cast "+cast_uri+" .\n"
            query += cast_uri+" mov:name '"+name+"' .\n"
    query += "}"

    print(query)
    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)
    
    return res['results']['bindings']


def deleteByTitle(title):
    query = """
        PREFIX mov:<http://netflixUA.org/>

        DELETE { 
            ?title_id ?p ?o .
            ?director_id ?director_p ?director_o .
            ?genre_id ?genre_p ?genre_o .
            ?country_id ?country_p ?country_o .
            ?person_id ?person_p ?person_o .
            }
            WHERE {
                ?title_id mov:title "teste" .
                ?title_id ?p ?o .
                OPTIONAL {
                    ?title_id mov:director ?director_id .
                }
                OPTIONAL {
                    ?title_id mov:listed_in ?genre_id .
                }
                OPTIONAL {
                    ?title_id mov:country ?country_id .
                }
                OPTIONAL {
                    ?title_id mov:cast ?person_id .
                }
            }
        }
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
    res = json.loads(res)

    return res['results']['bindings']


# def searchByTitleOrPerson(input):
#     query = """
#         PREFIX mov:<http://netflixUA.org/>
        
#         """
    
#     payload_query = {"query": query}
#     res = accessor.sparql_select(body=payload_query,repo_name=repo_name)
#     res = json.loads(res)

#     return res['results']['bindings']
