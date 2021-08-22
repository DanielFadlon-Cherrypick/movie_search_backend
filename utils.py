def filter_movie_short(dirty_movies):
    filter_movies = []
    if dirty_movies.get("Response"):
        dirty_movies = dirty_movies.get("Search")
        for movie in dirty_movies:
            filter_movies.append({
                'id': movie.get('imdbID'),
                'title': movie.get('Title'),
                'year': movie.get('Year'),
                'poster': movie.get('Poster')
            })
    return filter_movies


def filter_movie_details(movie):
    details_lst = ["title", "genre", "plot", "year", "country", "type", "boxOffice", "runtime", "actors", "awards", "metaScore", "poster"]
    filter_movie = {
        detail: movie.get(change_first_letter_to_capital(detail)) for detail in details_lst
    }
    filter_movie['id'] = movie.get("imdbID")

    return filter_movie


def change_first_letter_to_capital(value):
    letter = value[0]
    capital = chr(ord(letter) - 32)
    return capital + value[1:]
