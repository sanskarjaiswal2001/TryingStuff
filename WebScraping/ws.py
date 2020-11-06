import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=India'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='SearchResults')

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems :
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(company_elem.text)
    print(location_elem.text)
    print()
    
    