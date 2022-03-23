import time
import requests
import json
from app.methods import generate_random_movie
from flask import redirect
from app import app



@app.route('/api')
def home():
    return {'msg': "Hello, World!"}


@app.route('/api/generate-movie')
def generate_movie():
    random_movie = generate_random_movie()
    return redirect('/api/search-movie/' + random_movie)


@app.route('/api/search-movie/<title>')
def search_movie(title):
    url = "http://www.omdbapi.com/?t=" + title + "&apikey=e234192c"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'Title' in data and 'BoxOffice' in data:
            return {"Title": data['Title'],
                    "Director": data['Director'],
                    "ReleaseDate": data['Released'],
                    "Runtime" : data['Runtime'],
                    "imdbRating" : data['imdbRating'],
                    "BoxOfficeGross": data['BoxOffice']}\
                , 200
        else:
            return "FAIL - no movie", 404
    else:
        return "uh oh... other fail", 404

