from pymongo import MongoClient

# connect to database
client = MongoClient(
    'mongodb+srv://dbUser:DF18traindata@cluster0.impm7.mongodb.net/movies?retryWrites=true&w=majority&authSource=admin'
)

db = client.movies


def get_favorite_movies():
    collection_items = []
    try:
        data = db['FavoriteMovies'].find({})
    except Exception as err:
        raise err
    for item in data:
        item.pop('_id')
        collection_items.append(item)
    return collection_items


def add_favorite_movie(favorite_movie):
    movies = get_favorite_movies()
    for movie in movies:
        if movie['id'] == favorite_movie['id']:
            return
    db['FavoriteMovies'].insert_one(favorite_movie)


def delete_movie(movie_id):
    try:
        db['FavoriteMovies'].delete_one({"id": movie_id})
    except Exception as err:
        raise err
