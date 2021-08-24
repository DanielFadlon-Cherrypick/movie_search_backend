import requests


def get_movies(params):
    response = requests.get('https://movie-database-imdb-alternative.p.rapidapi.com/',
                            params=params,
                            headers={
                                'x-rapidapi-host': 'movie-database-imdb-alternative.p.rapidapi.com',
                                'x-rapidapi-key': 'f80ac4d453msh0bf3e3080de58b9p192bcfjsn86ef8518a220'
                            }
                            )
    if response.status_code == 200:
        return response.json()
    else:
        return None


def search_movies_by_title(search_value):
    params = {'s': search_value, 'r': 'json'}
    return get_movies(params)


def get_movie_by_id(search_value):
    params = {'i': search_value, 'r': 'json'}
    response = get_movies(params)
    if response.get("Response") == "True":
        return response
    else:
        return None

