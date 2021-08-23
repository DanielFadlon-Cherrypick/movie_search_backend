import json
from flask import Flask, request
from flask_cors import CORS
from request import search_movies_by_title, get_movie_by_id
from utils import filter_movie_short, filter_movie_details


def create_app():
    app = Flask(__name__)
    app.secret_key = "super secret key"
    CORS(app)

    @app.route('/movies', methods=['GET'])
    def main_screen():
        if request.method == 'GET':
            search_value = request.args.get('search_value')
            movies = filter_movie_short(search_movies_by_title(search_value))
            return json_response(movies)

    @app.route('/movies/<movie_id>', methods=['GET'])
    def movie_scr(movie_id):
        if request.method == 'GET':
            movie = filter_movie_details(get_movie_by_id(movie_id))
            return json_response(movie)

    def json_response(payload, status=200):
        return json.dumps(payload), status, {'content-type': 'application/json'}

    return app