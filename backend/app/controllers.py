from bs4 import BeautifulSoup
from selenium import webdriver


def generate_random_movie():
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