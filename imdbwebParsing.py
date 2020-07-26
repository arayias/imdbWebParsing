#!/usr/bin/env python
# coding: utf-8



from requests import get
from bs4 import BeautifulSoup

# obtain html via requests
for i in range(15,21): # year 2015-2020
    url = f'http://www.imdb.com/search/title?release_date=20{i}&sort=num_votes,desc&page=1' #only displaying page one to show top 50
    response = get(url)

    #parse html via beautiful soup
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

    for i in range(len(movie_containers)):
        name = movie_containers[i].h3.a.text #locates title
        year = movie_containers[i].find('span', class_ = 'lister-item-year text-muted unbold').text #locates year
        imdbRating = movie_containers[i].find('div', class_ = 'inline-block ratings-imdb-rating').strong.text #locates rating
        genre = (movie_containers[i].find('span', class_ = 'genre').text).strip() #locates genre



        print(f'{name} , {year} , {imdbRating} , ({genre})')
    
