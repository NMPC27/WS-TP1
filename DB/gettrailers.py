import requests
from pprint import pprint
import json
import time
theMovie_api_key = "c08d35426ff385e63e4b2657a12bafea"

dict = json.loads(open('test.json').read())
f=open('trailers.csv','a')

for idx,show in enumerate(dict):
    show_uri= f'<http://netflixUA.org/show/{dict[show]["id"]}>' 
    if dict[show]["type"] == "TV Show":
        url = "https://api.themoviedb.org/3/search/tv?api_key="+theMovie_api_key+"&query="+show

    else:
        url = "https://api.themoviedb.org/3/search/movie?api_key="+theMovie_api_key+"&query="+show
        
    response = requests.get(url)
    dict_values = json.loads(response.text)
    if dict_values['total_results'] == 0:
        
        f.write(f'{show_uri} <http://netflixUA.org/trailer> "N/A" .\n')
        print(f'{idx+1} no results    ', end='\n')
        
        continue
    else:
        dict_values = dict_values['results'][0]
        id=dict_values['id']
        if dict[show]["type"] == "TV Show":
            url = "https://api.themoviedb.org/3/tv/"+str(id)+"/videos?api_key="+theMovie_api_key
        else:
            url = "https://api.themoviedb.org/3/movie/"+str(id)+"/videos?api_key="+theMovie_api_key
            
        response = requests.get(url)
        dict_values = json.loads(response.text)
        if dict_values['results'] == []:
            f.write(f'{show_uri} <http://netflixUA.org/trailer> "N/A" .\n')
            print(f'{idx+1} no results    ', end='\n')
            continue
        
        trailer=''
        for item in dict_values['results']:
            if item['type'] == 'Trailer':
                trailer=item['key']
                break
        if trailer == '':
            #try to find teaser
            for item in dict_values['results']:
                if item['type'] == 'Teaser':
                    trailer=item['key']
                    print(f'{idx+1} found teaser', end='\n')
                    break
        
        if trailer == '':
            f.write(f'{show_uri} <http://netflixUA.org/trailer> "N/A" .\n')
            print(f'{idx+1} no results    ', end='\n')
            continue
        else:
            f.write(f'{show_uri} <http://netflixUA.org/trailer> "{trailer}" .\n')
            print(f'{idx+1} found trailer', end='\r')
            
   
    
    # print(f'{show_uri} <http://netflixUA.org/rating> "{result}" .\n')