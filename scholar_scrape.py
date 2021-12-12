from bs4 import BeautifulSoup
import requests

# get html for a person's profile on google scholar
html_text = requests.get('https://scholar.google.com/citations?hl=en&user=6mSbTDgAAAAJ').text
soup = BeautifulSoup(html_text, 'lxml')
# store all of their publications in an array
publications = soup.find_all('tr', class_='gsc_a_tr')
# loop through publications
for publication in publications:
    # access publication title
    title = publication.td.a.text
    print(title)
    divs = publication.find_all('div', class_='gs_gray')
    # access publication authors (i should probably store each author individually but i haven't tried to yet)
    authors = divs[0].text
    # get publication citation info
    citation = divs[1].text
    print(authors)
    print(citation)
    # get publication year
    year = publication.find('td', class_='gsc_a_y').text
    print(year)
    # get publication link
    link = 'https://scholar.google.com' + str(publication.td.a['href'])
    print(link)        
    print('')
