import re

def validate_request(request):
    returndict = {k: v for k, v in request.items() if v}
    if returndict.get('page') and not returndict.get('page').isdigit():
        returndict['page'] = 1
    if returndict.get('page') and int(returndict.get('page')) < 1:
        returndict['page'] = 1
        
    if returndict.get('type'):
        type_mapping = {
            'Movie': 'Movie',
            'TV Show': 'TV Show',
            'Movies': 'Movie',
            'Tv Shows': 'TV Show'
        }
        returndict['type'] = type_mapping.get(returndict['type'], 'All')

        
    if returndict.get('rating'):
        if re.match(r'(\d)\.(\d)', returndict.get('rating')):
            rating = returndict.get('rating').split('.')[0]
            returndict['rating'] = f"{rating}-{str(int(rating)+1)}"
        elif re.match(r'(\d)\-(\d)', returndict.get('rating')):
            n1, n2 = returndict.get('rating').split('-')
            if int(n1) > int(n2):
                returndict['rating'] = "All"
            if int(n1) < 0 or int(n2) > 10:
                returndict['rating'] = "All"
        else:
            returndict['rating'] = "All"       
            
        
    return returndict