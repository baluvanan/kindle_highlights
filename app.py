from bs4 import BeautifulSoup
import json
import os
DIRECTORY = './highlights'

def parse_highlights(fileName):
    html_doc = open('{}/{}'.format(DIRECTORY,fileName))
    soup = BeautifulSoup(html_doc.read())
    #print(soup.prettify())
    bookTitle = (soup.find('div',{"class":"bookTitle"})).text.strip()
    author = (soup.find('div',{"class":"authors"})).text.strip()
    highlights = soup.find_all('div',{"class":"noteText"})
    highlight_list = []
    for each_highlight in highlights:
        #print(each_highlight.text)
        highlight_list.append(each_highlight.text.strip())
    #print(highlights)
    data = {"title":bookTitle,"author":author,"highlights":highlight_list}
    with open('{}.json'.format(bookTitle), 'w') as outfile:
        json.dump(data, outfile)

files = os.listdir(DIRECTORY)
for file in files:
    parse_highlights(file)


#json_data = json.dumps(data)

#print(json_data)
