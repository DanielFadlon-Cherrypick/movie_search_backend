import json
from flask import Flask, request
from flask_cors import CORS
from request import search_movies_by_title, get_movie_by_id
from utils import filter_movie_short, filter_movie_details
from handleMongo import get_favorite_movies, add_favorite_movie, delete_movie


def create_app():
    app = Flask(__name__)
    app.secret_key = "super secret key"
    CORS(app)

    @app.route('/movies', methods=['GET'])
    def search_movie():
        try:
            search_value = request.args.get('value')
            movies = search_movies_by_title(search_value)
        except Exception as err:
            return error_response(err, 500)

        if movies['Response'] == 'False':
            return json_response([])

        return json_response(filter_movie_short(movies))

    @app.route('/movies/<movie_id>', methods=['GET'])
    def get_movie(movie_id):
        try:
            movie = get_movie_by_id(movie_id)
            if movie is None:
                return error_response("Movie Not Found! probably, wrong movie_id number", 400)
            return json_response(filter_movie_details(movie))
        except Exception as err:
            return error_response(err, 500)

    @app.route('/add_to_favorites', methods=['POST'])
    def add_favorite():
        try:
            movie_id = request.args.get('movie_id')
            movie = get_movie_by_id(movie_id)
            if movie is None:
                return error_response("Movie Not Found! probably, wrong movie_id number", 400)

            add_favorite_movie(filter_movie_details(movie))
            return json_response("SUCCESS")
        except Exception as err:
            return error_response(err, 500)

    @app.route('/favorites', methods=['GET'])
    def get_favorites():
        try:
            collection = get_favorite_movies()
            return json_response(collection)
        except Exception as err:
            return error_response(err, 500)

    @app.route('/delete_movie_from_favorites', methods=['POST'])
    def delete_movie_from_favorites():
        try:
            movie_id = request.args.get('movie_id')
            delete_movie(movie_id)
            return json_response("SUCCESS")
        except Exception as err:
            return error_response(err, 500)

    def json_response(payload, status=200):
        return json.dumps(payload), status, {'content-type': 'application/json'}

    def error_response(err, status):
        return {"error": str(err)}, status, {'content-type': 'application/json'}

    return app
