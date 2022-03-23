
import requests
from app.controllers import generate_random_movie_, search_movie_, compare_movies_
from flask import redirect
from app import app



@app.route('/api')
def home():
    return {'msg': "Hello, World!"}


@app.route('/api/generate-movie')
def generate_movie():
    random_movie = generate_random_movie_()
    return redirect('/api/search-movie/' + random_movie)


@app.route('/api/search-movie/<title>')
def search(title):
    results = search_movie_(title)
    if results:
        return results.jsonify(), 200
    else:
        return "FAIL", 404


@app.route('/api/compare-movies/<guess>/<target>')
def compare(guess, target):

    comparison_result = compare_movies_(guess, target)
    if comparison_result:
        return comparison_result.jsonify(), 200
    else:
        return "FAIL", 404
