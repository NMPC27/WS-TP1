
#convert csv to rdf
import csv
from time import sleep
from datetime import datetime

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
    #fix unknown values
    all_triples += f'<http://netflixUA.org/director/unknown> <http://netflixUA.org/name> "UNKNOWN" .\n'
    all_triples += f'<http://netflixUA.org/country/unknown> <http://netflixUA.org/name> "UNKNOWN" .\n'
    all_triples += f'<http://netflixUA.org/listed_in/unknown> <http://netflixUA.org/name> "UNKNOWN" .\n'
    
    genreDict = {
        "Documentaries" : "Documentary",
        "International TV Shows" : "International",
        "TV Dramas" : "Drama",
        "TV Mysteries" : "Mystery",
        "Crime TV Shows" : "Crime",
        "TV Action & Adventure" : "Action & Adventure",
        "Docuseries" : "Documentary",
        "Reality TV" : "Reality Show",
        "Romantic TV Shows" : "Romance",
        "TV Comedies" : "Comedy",
        "TV Horror" : "Horror",
        "Children & Family Movies" : "Children & Family",
        "Dramas" : "Drama",
        "Independent Movies" : "Independent",
        "International Movies" : "International",
        "British TV Shows" : "British",
        "Comedies" : "Comedy",
        "Spanish-Language TV Shows" : "Spanish",
        "Thrillers" : "Thriller",
        "Romantic Movies" : "Romance",
        "Music & Musicals" : "Music & Musical",
        "Horror Movies" : "Horror",
        "Sci-Fi & Fantasy" : "Sci-Fi & Fantasy",
        "TV Thrillers" : "Thriller",
        "Kids' TV" : "Children & Family",
        "Action & Adventure" : "Action & Adventure",
        "TV Sci-Fi & Fantasy" : "Sci-Fi & Fantasy",
        "Classic Movies" : "Classic",
        "Anime Features" : "Anime",
        "Sports Movies" : "Sports",
        "Anime Series" : "Anime",
        "Korean TV Shows" : "Korean",
        "Science & Nature TV" : "Science & Nature",
        "Teen TV Shows" : "Teen",
        "Cult Movies" : "", #! se estragar mudar
        "TV Shows" : "",  #! se estragar mudar
        "Faith & Spirituality" : "Faith & Spirituality",
        "LGBTQ Movies" : "LGBTQ",
        "Stand-Up Comedy" : "Comedy",
        "Movies" : "", #! se estragar mudar
        "Stand-Up Comedy & Talk Shows" : "Comedy",
        "Classic & Cult TV" : "", #! se estragar mudar
    }
    
    
    once = set()
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
        # print(show_id)
        if(show_id == "0"): # s8421
            break
        # Convert the show_id field to an N-Triples URI
        show_uri = f'<http://netflixUA.org/show/{show_id}>' 
        
        # Create (title)
        #remove quotes from title
        title = title.replace('"','\\"')
        title_literal = f'"{title}"'
        triples = f'{show_uri} <http://netflixUA.org/title> {title_literal} . \n'
        
        #create all directors
        if director == "":
            director = "UNKNOWN"
            
        director_split = director.split(",")
        for direct in director_split:
            dir = direct.strip().replace('"','').replace(" ","_").replace(".","")
            director_uri = f'<http://netflixUA.org/director/{dir.lower()}>'
            triples += f'{show_uri} <http://netflixUA.org/director> {director_uri} . \n'
            if dir not in once:
                triples += f'{director_uri} <http://netflixUA.org/name> "{dir.replace("_"," ")}" .\n'
                once.add(dir)
            
        #create all cast
        if cast == "":
            cast = "UNKNOWN"
            
        cast_split = cast.split(",")
        for c in cast_split:
            c = c.strip().replace('"','').replace(" ","_").replace(".","")
            
            cast_uri = f'<http://netflixUA.org/cast/{c.strip().replace(" ","_").lower()}>'
            triples += f'{show_uri} <http://netflixUA.org/cast> {cast_uri} . \n'
            if c not in once:
                triples += f'{cast_uri} <http://netflixUA.org/name> "{c.strip().replace("_"," ")}" .\n'
                once.add(c)

            
        # Create (type)
        triples += f'{show_uri} <http://netflixUA.org/type> "{typeUA}" . \n'

        # Create (country)  
        if country == "":
            country = "UNKNOWN"
            
        country_split = country.split(",")
        for c in country_split:
            c = c.strip().replace('"','').replace(" ","_").replace(".","")

            country_uri = f'<http://netflixUA.org/country/{c.lower()}>'

            triples += f'{show_uri} <http://netflixUA.org/country> {country_uri} . \n'
            if c not in once:
                triples += f'{country_uri} <http://netflixUA.org/name> "{c.replace("_"," ")}" .\n'
                once.add(c)
    
        # Create (date_added)
        if date_added == "":
            date_added = "UNKNOWN"
            triples += f'{show_uri} <http://netflixUA.org/date_added> "{date_added}" . \n'
        else:
            date_obj = datetime.strptime(date_added.strip(), "%B %d, %Y")
            date_formatted = date_obj.strftime("%Y-%m-%d")
            triples += f'{show_uri} <http://netflixUA.org/date_added> "{date_formatted}" . \n'

        # Create (release_year)
        if release_year == "":
            release_year = "UNKNOWN"    
        release_year_literal = f'"{release_year}"'
        triples += f'{show_uri} <http://netflixUA.org/release_year> {release_year_literal} . \n'

        # Create (rating)
        if rating == "":
            rating = "UNKNOWN"
        rating_literal = f'"{rating}"'
        triples += f'{show_uri} <http://netflixUA.org/rating> {rating_literal} . \n'

        # Create (duration)
        if duration == "":
            duration = "UNKNOWN"
        duration_literal = f'"{duration}"'
        triples += f'{show_uri} <http://netflixUA.org/duration> {duration_literal} . \n'

        # Create (listed_in)
        if listed_in == "":
            listed_in = "UNKNOWN"
        listed_in_split = listed_in.split(",")
        for l in listed_in_split:
            l = genreDict[l.strip()]
            if l == "":
                continue
            
            l = l.strip().replace('"','').replace(" ","_").replace(".","")

            listed_in_uri = f'<http://netflixUA.org/listed_in/{l.lower()}>'

            triples += f'{show_uri} <http://netflixUA.org/listed_in> {listed_in_uri} . \n'
            if l not in once:
                triples += f'{listed_in_uri} <http://netflixUA.org/name> "{l.replace("_"," ")}" .\n'
                once.add(l)
        
        # Create (description)
        if description == "":
            description = "UNKNOWN"
        #remove all carriage returns and new lines
        desc = description.replace("\r","").replace("\n","")
        #escape all quotes
        desc = desc.replace('"','\\"')
        desc = desc.replace("'","\\'")
        
        description_literal = f'"{desc}"'
        triples += f'{show_uri} <http://netflixUA.org/description> {description_literal} . \n'

        print(show_id)
            
        all_triples += triples

    #export all triples to file
    with open("netflix_triples.nt", "w", encoding="utf-8") as f:
        # print(all_triples)
        f.write(all_triples)
        
        #open movies_img.csv and TVshow_img.csv
        with open("movies_img.csv", "r", encoding="utf-8") as f1:
            #copy everything from movies_img.csv to netflix_triples.nt
            f.write(f1.read())
        with open("TVshow_img.csv", "r", encoding="utf-8") as f2:
            #copy everything from TVshow_img.csv to netflix_triples.nt
            f.write(f2.read())
        

        f.close()
        f1.close()
        f2.close()
