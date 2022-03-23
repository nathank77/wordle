from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from app.models import Movie
from datetime import datetime


def generate_random_movie_():
    url = "https://www.bestrandoms.com/random-movie-generator"

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("/Users/nathankowal/Projects/wordle/backend/chromedriver", chrome_options=options)

    driver.get(url)

    elem = driver.find_element_by_class_name("spinner")
    elem = elem.find_element_by_class_name("form-control")
    elem.clear()
    elem.send_keys("1")

    elem = driver.find_element_by_css_selector("div[class='col-xs-offset-4 col-xs-8 col-sm-offset-4 col-sm-8']")
    elem = elem.find_element_by_class_name("btn-blue")
    elem.click()

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    movie_list = soup.find('li', class_="col-md-6")
    movie = movie_list.find('b')
    movie_title = movie.find('span').get_text()

    driver.close()
    return movie_title.split('(')[0]


def search_movie_(title):
    url = "http://www.omdbapi.com/?t=" + title + "&apikey=e234192c"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'Title' in data and 'BoxOffice' in data:

            release = datetime.strptime(data['Released'], "%d %b %Y")
            runtime = [int(s) for s in data['Runtime'].split() if s.isdigit()][0]

            txt = data['BoxOffice'].split('$')[1].split(',')
            txt = ''.join(txt)
            box_office = float(txt)

            movie = Movie(data['Title'],
                          data['Director'],
                          release,
                          runtime,
                          float(data['imdbRating']),
                          box_office)
            return movie
    return False


def compare_movies_(guess, target):
    guess = search_movie_(guess)
    target = search_movie_(target)

    if not guess or not target:
        return False

    return guess == target
