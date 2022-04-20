from requests_html import HTMLSession
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time
from nltk import tokenize

def get_works(search_tags):
    works = []
    for search_tag in search_tags:
        url = f'https://archiveofourown.org/works/search?work_search%5Bquery%5D=&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D={search_tag}&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=kudos_count&work_search%5Bsort_direction%5D=desc&commit=Search'
        print("Searching for works with tag: " + search_tag)

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        success = False
        retries = 0
        failure = False
        while not success and retries <= 5:
                try:
                    request_page = urlopen(req)
                    page_html = request_page.read()
                    request_page.close()
                    soup = BeautifulSoup(page_html, 'html.parser')
                    success = True
                except Exception as e:
                    if 'Retry-After' in e.headers:
                        wait = int(e.headers['Retry-After'])
                        success = False
                        print(f'Request limit reached.. Waiting {wait} seconds')
                        time.sleep(wait)
                    else:
                        wait = retries * 30
                        print(f'Error occured. Waiting {wait} secs and retrying.')
                        print(e)
                        time.sleep(wait)
                        success = False
                        retries += 1

        if not success and retries > 5:
            failure = True

        if not failure:
            results = soup.find('ol', class_='work index group').find_all('li', role='article')
            num_works = 0
            for result in results:
                new_url = 'https://archiveofourown.org' + result.a.get('href') + '?view_full_work=true&view_adult=true'
                if new_url not in works:
                    works.append(new_url)
                    num_works += 1
                if num_works > 5:
                    break
                
            ao3_works = open('ao3_works.txt', 'w', encoding="utf-8")
            
            for work in works:
                ao3_works.write(work + '\n')

            ao3_works.close()
    return works

def scrape_works(works):
    emet_ao3 = open('emet_ao3.txt', 'w', encoding='utf-8')

    for url in works:
        print("Scraping work: " + url)
        success = False
        retries = 0
        failure = False
        while not success and retries <= 5:
                
                session = HTMLSession()
                r = session.get(url)
                if r.status_code == 200:
                    r.html.render(timeout=20)
                    soup = BeautifulSoup(r.content, 'html.parser')
                    success = True
                elif r.status_code == 429:
                    if 'Retry-After' in r.headers:
                        wait = int(r.headers['Retry-After'])
                        success = False
                        print(f'Request limit reached.. Waiting {wait} seconds')
                        time.sleep(wait)
                    else:
                        wait = 300
                        print(f'Request limit reached, no Retry-After header was given. Waiting a default of {wait} seconds and retrying.')
                        time.sleep(wait)
                        success = False
                        retries += 1
                else:
                    wait = retries * 30
                    print(f'Error occured. Waiting {wait} secs and retrying.')
                    print(r)
                    time.sleep(wait)
                    success = False
                    retries += 1

        if not success and retries > 5:
            failure = True

        if not failure:
            content = soup.find('div', id='chapters').find_all('p')
            for ptag in content:
                tokens = tokenize.sent_tokenize(ptag.get_text())
                for token in tokens:
                    if 'Emet-Selch' in token or 'Hades' in token or 'Emet' in token:
                        emet_ao3.write('<|endoftext|>' + token + '<|endoftext|>\n')
            emet_ao3.write('\n')
        

if __name__ == '__main__':
    search_tags = [
        "Emet-Selch%2FWarrior+of+Light+%28Final+Fantasy+XIV%29",
        "Azem%2FEmet-Selch+%28Final+Fantasy+XIV%29",
        "Solus+zos+Galvus+%7C+Emet-Selch%2FSolus+zos+Galvus+%7C+Emet-Selch%27s+Wife",
        "Emet-Selch+%28Final+Fantasy+XIV%29%2FOriginal+Character%28s%29",
        "Emet-Selch+%26+Warrior+of+Light+%28Final+Fantasy+XIV%29",
        "Emet-Selch%2FHythlodaeus+%28Final+Fantasy+XIV%29",
        "Emet-Selch+%28Final+Fantasy+XIV%29%2FReader",
        "Azem%2FEmet-Selch%2FHythlodaeus+%28Final+Fantasy+XIV%29",
        "Emet-Selch%2FG%27raha+Tia+%7C+Crystal+Exarch",
        "Elidibus%2FEmet-Selch%2FWarrior+of+Light+%28Final+Fantasy+XIV%29"
    ]

    works = get_works(search_tags)

    scrape_works(works)


