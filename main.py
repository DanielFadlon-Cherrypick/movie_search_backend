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
        if request.method == 'GET':
            search_value = request.args.get('value')
            movies = search_movies_by_title(search_value)
            if movies['Response'] == 'False':
                return json_response([])

            return json_response(filter_movie_short(movies))

    @app.route('/movies/<movie_id>', methods=['GET', 'POST'])
    def get_movie(movie_id):
        if request.method == 'GET':
            movie = filter_movie_details(get_movie_by_id(movie_id))
            return json_response(movie)

    @app.route('/add_to_favorites', methods=['POST'])
    def add_favorite():
        if request.method == 'POST':
            movie_id = request.args.get('movie_id')
            movie = filter_movie_details(get_movie_by_id(movie_id))
            add_favorite_movie(movie)
            return json_response("SUCCESS")

    @app.route('/favorites', methods=['GET'])
    def get_favorites():
        if request.method == 'GET':
            return json_response(get_favorite_movies())

    @app.route('/delete_movie_from_favorites', methods=['POST'])
    def delete_movie_from_favorites():
        if request.method == 'POST':
            movie_id = request.args.get('movie_id')
            delete_movie(movie_id)
            return json_response("SUCCESS")

    def json_response(payload, status=200):
        return json.dumps(payload), status, {'content-type': 'application/json'}

    return app
