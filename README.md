# WS-TP1

##Install dependencies
`pip install -r requirements.txt`

Alternatively, you can just install the dependencies manually:
```bash
pip install Django
pip install s4api
```

##Setup database
1. Import DB/netflix_triples.net into GraphDB repository named "movies"
2. Set base IRI to `http://netflixUA.org`

If the port of GraphDB is not the default 7200 or the chosen repository name is different, please update the `config.json` file at the root of the project.

##Run server
The only dependencies are Django and s4api, if those are already installed
```bash
cd webApp
python3 manage.py runserver
```

In the case of ==static files not being served== , instead run:
`python3 manage.py runserver --insecure`

The webApp will be running on `http://localhost:8000`
