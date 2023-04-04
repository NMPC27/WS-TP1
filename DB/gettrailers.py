import requests
from pprint import pprint
import json
import time
theMovie_api_key = "c08d35426ff385e63e4b2657a12bafea"

dict = json.loads(open('../test.json').read())
f=open('ratings.csv','a')
i=0
for show in dict:
    show_uri= f'<http://netflixUA.org/show/{dict[show]["id"]}>' 
    if dict[show]["type"] == "TV Show":
        url = "https://api.themoviedb.org/3/search/tv?api_key="+theMovie_api_key+"&query="+show
    else:
        url = "https://api.themoviedb.org/3/search/movie?api_key="+theMovie_api_key+"&query="+show
    response = requests.get(url)
    dict_values = json.loads(response.text)
    if dict_values['total_results'] == 0:
        
        f.write(f'{show_uri} <http://netflixUA.org/rating> "N/A" .\n')
        continue
    else:  
        dict_values = dict_values['results'][0]
        result = round(dict_values['vote_average'],1)
        f.write(f'{show_uri} <http://netflixUA.org/rating> "{result}" .\n')
    i+=1
    print(i, end='\r')
    
    # print(f'{show_uri} <http://netflixUA.org/rating> "{result}" .\n')
print(i)