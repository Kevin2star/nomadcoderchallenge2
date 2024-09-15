import requests
from bs4 import BeautifulSoup

def scrape_berlinstartupjobs(search_term):
    url = f"https://berlinstartupjobs.com/skill-areas/{search_term}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('div', class_='item-body')
    results = []
    for job in jobs:
        title = job.find('h4', class_='title').text.strip()
        company = job.find('a', class_='company').text.strip()
        results.append({'title': title, 'company': company, 'source': 'Berlin Startup Jobs'})
    return results

def scrape_weworkremotely(search_term):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={search_term}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('li', class_='feature')
    results = []
    for job in jobs:
        title = job.find('span', class_='title').text.strip()
        company = job.find('span', class_='company').text.strip()
        results.append({'title': title, 'company': company, 'source': 'We Work Remotely'})
    return results

def scrape_web3career(search_term):
    url = f"https://web3.career/{search_term}-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('div', class_='job_list_item')
    results = []
    for job in jobs:
        title = job.find('h2', class_='job_title').text.strip()
        company = job.find('div', class_='company_name').text.strip()
        results.append({'title': title, 'company': company, 'source': 'Web3 Career'})
    return results

def scrape_all(search_term):
    results = []
    results.extend(scrape_berlinstartupjobs(search_term))
    results.extend(scrape_weworkremotely(search_term))
    results.extend(scrape_web3career(search_term))
    return results