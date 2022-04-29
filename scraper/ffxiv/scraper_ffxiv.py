#Scrapes garland tools for all quests from beginning of Shadowbringers to (current) end of Endwalker, that relate to Emet-Selch

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time

dialogue_emet = open('./dialogue_emet.txt', 'w', encoding="utf-8")
dialogue_others = open('./dialogue_others.txt', 'w', encoding="utf-8")
#Links to each patch's questlines. Having individual, hardcoded links seemed easier
urls = [
    #Shadowbringers 
    "https://ffxiv.gamerescape.com/wiki/Main_Scenario_Quests/Shadowbringers",
    "https://ffxiv.gamerescape.com/wiki/Main_Scenario_Quests/Vows_of_Virtue,_Deeds_of_Cruelty",
    "https://ffxiv.gamerescape.com/wiki/Main_Scenario_Quests/Echoes_of_a_Fallen_Star",
    "https://ffxiv.gamerescape.com/wiki/Main_Scenario_Quests/Reflections_in_Crystal",
    "https://ffxiv.gamerescape.com/wiki/Main_Scenario_Quest/Futures_Rewritten",
    "https://ffxiv.gamerescape.com/wiki/Main_Scenario_Quest/Death_Unto_Dawn",
    #Endwalker
    "https://ffxiv.gamerescape.com/wiki/Main_Scenario_Quest/Endwalker",
    "https://ffxiv.gamerescape.com/wiki/Main_Scenario_Quest/Newfound_Adventure"
]
for url in urls:
    print("Start of " + url[url.rfind('/')+1:] + ".")
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    request_page = urlopen(req)
    page_html = request_page.read()
    request_page.close()

    soup = BeautifulSoup(page_html, 'html.parser')
    #print(soup)
    table = soup.find_all('tbody')[1]
    #print(table)
    results = table.find_all('tr')
    
    #Go through every quest 
    for i in range(1, len(results)):
        print(f'Currently running on Quest {i} of {len(results)-1}')
        #Find the atag the references to current quest, get the url and make the request.
        atag = results[i].find('a')
        quest = atag.get_text()
        newurl = atag.get('href')
        url = "https://ffxiv.gamerescape.com" + newurl
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

        if failure:
            print(f'Error.. Failed to load quest: {quest}, skipping.')
        else:
            #Finds the dialogue div
            soup = BeautifulSoup(page_html, 'html.parser').select('div[title="Dialogue"]')
            #Gets all the dialogue (Usable dialogue will be [1,len(dialogue)-1])
            dialogue = soup[0].find_all('table', class_=False)

            #Go through all the dialogue in this quest
            for j in range(1, len(dialogue)):
                #Split the dialogue box.. bubbles[0] should be the person speaking, bubbles[1] should be what was said
                bubbles = dialogue[j].find_all('div', class_='bubble')
                if len(bubbles) > 1:
                    speaker = bubbles[0].get_text()
                    speech = bubbles[1].get_text().split('\n')
                    if speaker == 'Emet-Selch' or speaker == 'Hades':
                        dialogue_emet.write('<|endoftext|>Emet-Selch: ')
                        for sentence in speech:
                            if len(sentence) > 0:
                                dialogue_emet.write(sentence + ' ')
                        dialogue_emet.write('<|endoftext|>\n')

                    if any('Emet-Selch' in sentence or 'Hades' in sentence for sentence in speech):
                        dialogue_others.write(f'<|endoftext|>{speaker}: ')
                        for sentence in speech:
                            if len(sentence) > 0:
                                dialogue_others.write(sentence + ' ')
                        dialogue_others.write('<|endoftext|>\n')
