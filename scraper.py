#Scrapes garland tools for all quests from beginning of Shadowbringers to (current) end of Endwalker, that relate to Emet-Selch

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

#Simple indexOf function since python's doesn't return -1 on fail
def has_no_class(tag):
    return not tag.has_attr('class')


dialogue_emet = open('./dialogue_emet.txt', 'w', encoding="utf-8")
dialogue_others = open('./dialogue_others.txt', 'w', encoding="utf-8")

url = "https://ffxiv.gamerescape.com/wiki/Main_Scenario_Quests/Shadowbringers"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
request_page = urlopen(req)
page_html = request_page.read()
request_page.close()

soup = BeautifulSoup(page_html, 'html.parser')
#print(soup)
table = soup.find_all('tbody')[1]
#print(table)
results = table.find_all('tr')

#Go through every quest of Shadowbringers (should be 109 quests/pages)
for i in range(1, 110):
    print(f'Currently running on Quest {i} of {109}')
    #Find the atag the references to current quest, get the url and make the request.
    atag = results[i].find('a')
    quest = atag.get_text()
    newurl = atag.get('href')
    url = "https://ffxiv.gamerescape.com" + newurl
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    request_page = urlopen(req)
    page_html = request_page.read()
    request_page.close()

    #Finds the dialogue div
    soup = BeautifulSoup(page_html, 'html.parser').select('div[title="Dialogue"]')
    #Gets all the dialogue (Usable dialogue will be [1,len(dialogue)-1])
    dialogue = soup[0].find_all('table', class_=False)

    dialogue_emet.write(f'CURRENT QUEST: {quest}\n')
    dialogue_others.write(f'CURRENT QUEST: {quest}\n')


    #Go through all the dialogue in this quest
    for j in range(1, len(dialogue)):
        #Split the dialogue box.. bubbles[0] should be the person speaking, bubbles[1] should be what was said
        bubbles = dialogue[j].find_all('div', class_='bubble')
        if len(bubbles) > 1:
            speaker = bubbles[0].get_text()
            speech = bubbles[1].get_text().split('\n')
            if speaker == 'Emet-Selch':
                for sentence in speech:
                    if len(sentence) > 0:
                        dialogue_emet.write(sentence + ' ')
                dialogue_emet.write('\n')

            if any('Emet-Selch' in sentence for sentence in speech):
                dialogue_others.write(speaker + '\n')
                for sentence in speech:
                    if len(sentence) > 0:
                        dialogue_others.write(sentence + ' ')
                dialogue_others.write('\n\n')
