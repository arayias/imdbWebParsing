import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

# obtain html via requests
for x in range(17,19):
    done = False
    movieCounter = 1
    pageCounter = 1
    top = 100
    while True:
        
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        
        url = f'https://www.imdb.com/search/title/?release_date=20{x}-01-01,20{x}-12-31&sort=num_votes,desc&start={movieCounter}&ref_=adv_nxt'
        print(url)
        response = requests.get(url)

        #parse html via beautiful soup
        html_soup = BeautifulSoup(response.text, 'html.parser')
        type(html_soup)

        movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
        
#         if not done: #initially done on first page to find out how many movies there are -- use to traverse whole pages - may time out if too many.
#             pages = html_soup.find('div', class_ = 'desc')
#             nofpages = int((pages.span.text.split()[2]).replace(',',''))
#             done = True

#         if nofpages // 50 != nofpages /50: nofpages = nofpages//50 +1
#         else: nofpages = nofpages//50
            
       

        for i in range(len(movie_containers)):
            name = movie_containers[i].h3.a.text
            year = movie_containers[i].find('span', class_ = 'lister-item-year text-muted unbold').text
            imdbRating = movie_containers[i].find('div', class_ = 'inline-block ratings-imdb-rating').strong.text
            genre = (movie_containers[i].find('span', class_ = 'genre').text).strip()



            print(f'{name} , {year} , {imdbRating} , ({genre}) \n')
        
#         if pageCounter == nofpages:
#             break
            
        
        
        movieCounter += 50
        pageCounter += 1
        
        
        if movieCounter == top+1:
            break
        print(pageCounter)
