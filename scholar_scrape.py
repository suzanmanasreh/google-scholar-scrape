from bs4 import BeautifulSoup
import requests
import json
import pprint

# get html for a person's profile on google scholar
html_text = requests.get(
    'https://scholar.google.com/citations?hl=en&user=6mSbTDgAAAAJ').text
soup = BeautifulSoup(html_text, 'lxml')
# store all of their publications in an array
publications = soup.find_all('tr', class_='gsc_a_tr')
# loop through publications

# We'll use this to pool together the publications and make the json
data = []

for publication in publications:
    curr_pub = {}
    # access publication title
    title = publication.td.a.text

    curr_pub["title"] = title
    divs = publication.find_all('div', class_='gs_gray')
    # access publication authors (i should probably store each author individually but i haven't tried to yet)
    authors = divs[0].text
    # get publication citation info
    citation = divs[1].text

    curr_pub["authors"] = authors
    curr_pub["citation"] = citation

    year = publication.find('td', class_='gsc_a_y').text

    curr_pub["year"] = year

    link = 'https://scholar.google.com' + str(publication.td.a['href'])

    curr_pub["link"] = link

    data.append(curr_pub)

s = json.dumps(data)
pprint.pprint(s)


with open('json_data.json', 'w') as f:
    f.write(s)
