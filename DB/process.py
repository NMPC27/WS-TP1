
#convert csv to rdf
import csv
from time import sleep

# create ids for each director or cast member

# show_id type STR(movie/tv show)   OK
# show_id title STR(nome filme)     OK
# show_id director ID(director)     OK
# show_id cast ID(cast)             OK
# ID(director) name STR(name)       OK
# ID(cast) name STR(name)           OK


# show_id country id(country)
# show_id date_added STR(date_added)
# show_id release_year INT(release_year)
# show_id rating STR(rating)
# show_id duration STR(duration)

## prof tem -> name,starrinf,directed_by
## nos temos -> title,cast,director,name,type,country,date_added,release_year,rating,duration,listed_in,description


#show_id,type,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description
# Open the CSV file
with open('netflix_titles.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    all_triples = ""
    # Loop through each row of the CSV file
    for row in reader:
        # Extract the data from each row
        show_id = row['show_id']
        typeUA = row['type']
        title = row['title']
        director = row['director']
        cast = row['cast']
        country = row['country']
        date_added = row['date_added']
        release_year = row['release_year']
        rating = row['rating']
        duration = row['duration']
        listed_in = row['listed_in']
        description = row['description']
        print(show_id)
        if(show_id == "s1000"):
            break
        # Convert the show_id field to an N-Triples URI
        show_uri = f'<http://netflixUA.org/show/{show_id}>' 
        
        # Create (title)
        title_literal = f'"{title}"'
        triples = f'{show_uri} <http://netflixUA.org/title> {title_literal} . \n'
        
        #create all directors
        if director == "":
            director = "UNKNOWN"
            
        director_split = director.split(",")
        for direct in director_split:
            dir = direct.strip().replace('"','').replace(" ","_")
            director_uri = f'<http://netflixUA.org/director/id_{dir}>'
            triples += f'{show_uri} <http://netflixUA.org/director> {director_uri} . \n'
            triples += f'{director_uri} <http://netflixUA.org/name> "{dir.replace("_"," ")}" .\n'
            
        #create all cast
        if cast == "":
            cast = "UNKNOWN"
            
        director_split = cast.split(",")
        for direct in director_split:
            dir = direct.strip().replace('"','').replace(" ","_")
            director_uri = f'<http://netflixUA.org/cast/id_{dir}>'
            triples += f'{show_uri} <http://netflixUA.org/cast> {director_uri} . \n'
            triples += f'{director_uri} <http://netflixUA.org/name> "{dir.replace("_"," ")}" .\n'
            
        # Create (type)
        triples += f'{show_uri} <http://netflixUA.org/type> "{typeUA}" . \n'
        all_triples += triples
    
    #export all triples to file
    with open("netflix_triples.nt", "w", encoding="utf-8") as f:
        # print(all_triples)
        f.write(all_triples)
        f.close()
        
        
# # Convert the show_id field to an N-Triples URI
# show_uri = f'<http://example.org/show/{show_id}>'

# # Convert the title field to an N-Triples literal
# title_literal = f'"{title}"'

# # Convert the director field to an N-Triples URI
# director_uri = f'<http://example.org/director/{director}>'

# # Combine the triples
# triples = f'{show_uri} <http://example.org/title> {title_literal} .\n'
# triples += f'{show_uri} <http://example.org/director> {director_uri} .'