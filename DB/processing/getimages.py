import requests
from pprint import pprint
import json
import time
theMovie_api_key = "c08d35426ff385e63e4b2657a12bafea"

dict = json.loads(open('test.json').read())
f=open('images.csv','a')
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
        
        f.write(f'{show_uri} <http://netflixUA.org/img> "NO_IMAGE" .\n')
        i+=1
        continue
    else:
        dict_values = dict_values['results'][0]
        if dict_values['poster_path'] == None:
            if dict_values['backdrop_path'] == None:
                f.write(f'{show_uri} <http://netflixUA.org/img> "NO_IMAGE" .\n')
                i+=1
                continue
            else:
                f.write(f'{show_uri} <http://netflixUA.org/img> "https://image.tmdb.org/t/p/w500'+dict_values['backdrop_path']+'" .\n')
                i+=1
                continue
        else:
            f.write(f'{show_uri} <http://netflixUA.org/img> "https://image.tmdb.org/t/p/w500'+dict_values['poster_path']+'" .\n')
            # print(f'{show_ur  i} <http://netflixUA.org/img> "https://image.tmdb.org/t/p/w500'+dict_values['poster_path']+'" .\n')
            i+=1

    print(i, end='\r')
    
    # print(f'{show_uri} <http://netflixUA.org/rating> "{result}" .\n')
print(i)