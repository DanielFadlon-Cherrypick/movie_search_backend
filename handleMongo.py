from pymongo import MongoClient

# connect to database
client = MongoClient(
    'mongodb+srv://dbUser:DF18traindata@cluster0.impm7.mongodb.net/movies?retryWrites=true&w=majority&authSource=admin'
)

db = client.movies


def get_favorite_movies():
    collection_items = []
    data = db['FavoriteMovies'].find({})
    for item in data:
        item.pop('_id')
        collection_items.append(item)
    return collection_items


def add_favorite_movie(favorite_movie):
    db['FavoriteMovies'].insert_one(favorite_movie)
