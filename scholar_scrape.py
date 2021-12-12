from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://scholar.google.com/citations?hl=en&user=6mSbTDgAAAAJ').text
soup = BeautifulSoup(html_text, 'lxml')
publications = soup.find_all('tr', class_='gsc_a_tr')
for publication in publications:
    title = publication.td.a.text
    print(title)
    divs = publication.find_all('div', class_='gs_gray')
    authors = divs[0].text
    citation = divs[1].text
    print(authors)
    print(citation)
    year = publication.find('td', class_='gsc_a_y').text
    print(year)
    link = 'https://scholar.google.com' + str(publication.td.a['href'])
    print(link)        
    print('')
