import pandas as pd
print('Data Scraping')
from bs4 import BeautifulSoup
from requests import get
url="https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=num_votes,desc&start=1&ref_=adv_nxt"

url_list=["https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=num_votes,desc&start=1&ref_=adv_nxt"]
for i in range(51,10000,50):
    url_list.append(url[:96]+str(i)+url[97:])
    

print(len(url_list))
response=[]
html_soup=[]
movie_containers=[]
for i in range(0,200):
    response.append(get(url_list[i]))
    html_soup.append(BeautifulSoup(response[i].text, 'html.parser'))
    movie_containers.append(html_soup[i].find_all('div',class_='lister-item-content'))
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
for i in range(0,200):
    for container in movie_containers[i]:
        if container.find('div', class_ = "ratings-metascore") is not None:
            name = container.h3.a.text
            names.append(name)
        
            year = container.h3.find('span', class_ = "lister-item-year").text
            years.append(year)
        
            imdb = float(container.strong.text)
            imdb_ratings.append(imdb)
        
            m_score = container.find('span', class_ = 'metascore').text
            metascores.append(m_score)
        
            vote = container.find('span', attrs = {'name':'nv'})['data-value']
            votes.append(vote)
        
    
import pandas as pd
movies_df = pd.DataFrame({'Movie':names,
                         'year':years,
                         'metascore':metascores,
                         'rating':imdb_ratings,
                         'votes':votes})
print(movies_df)        