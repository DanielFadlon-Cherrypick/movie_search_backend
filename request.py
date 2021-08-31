import requests


def get_movies(params):
    try:
        response = requests.get('https://movie-database-imdb-alternative.p.rapidapi.com/',
                                params=params,
                                headers={
                                    'x-rapidapi-host': 'movie-database-imdb-alternative.p.rapidapi.com',
                                    'x-rapidapi-key': 'f80ac4d453msh0bf3e3080de58b9p192bcfjsn86ef8518a220'
                                }
                                )
        return response.json()
    except Exception as err:
        raise err


def search_movies_by_title(search_value):
    try:
        params = {'s': search_value, 'r': 'json'}
        return get_movies(params)
    except Exception as err:
        raise err


def get_movie_by_id(search_value):
    try:
        params = {'i': search_value, 'r': 'json'}
        response = get_movies(params)
        if response.get("Response") == "True":
            return response
        else:
            return None
    except Exception as err:
        raise err
