# WS-TP1

##Install dependencies
`pip install -r requirements.txt`

Alternatively, you can just install the dependencies manually:
```bash
pip install Django
pip install s4api
```

##Setup database
1. Import DB/netflix_triples.net into GraphDB
2. Set base IRI to `http://netflixUA.org`

##Run server
`python3 manage.py runserver`


In the case that ==static files are not being served== , run the following command instead:
`python3 manage.py runserver --insecure`

The server will be running on `http://localhost:8000`
