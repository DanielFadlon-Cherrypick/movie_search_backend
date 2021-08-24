import json
from flask import Flask, request
from flask_cors import CORS
from request import search_movies_by_title, get_movie_by_id
from utils import filter_movie_short, filter_movie_details
from handleMongo import get_favorite_movies, add_favorite_movie


def create_app():
    app = Flask(__name__)
    app.secret_key = "super secret key"
    CORS(app)

    @app.route('/movies', methods=['GET'])
    def main_screen():
        if request.method == 'GET':
            search_value = request.args.get('value')
            movies = filter_movie_short(search_movies_by_title(search_value))
            return json_response(movies)

    @app.route('/movies/<movie_id>', methods=['GET', 'POST'])
    def movie_scr(movie_id):
        movie = filter_movie_details(get_movie_by_id(movie_id))
        print(movie)
        if request.method == 'GET':
            return json_response(movie)
        if request.method == 'POST':
            add_favorite_movie(movie)
            return json_response("SUCCESS")

    @app.route('/favorites', methods=['GET'])
    def get_favorites():
        if request.method == 'GET':
            return json_response(get_favorite_movies())

    def json_response(payload, status=200):
        return json.dumps(payload), status, {'content-type': 'application/json'}

    return app