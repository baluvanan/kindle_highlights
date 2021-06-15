from bs4 import BeautifulSoup
import json
html_doc = open('./highlights/ikigai.html')
soup = BeautifulSoup(html_doc.read())
#print(soup.prettify())
bookTitle = soup.find('div',{"class":"bookTitle"})
author = soup.find('div',{"class":"authors"})
highlights = soup.find_all('div',{"class":"noteText"})
highlight_list = []
for each_highlight in highlights:
    #print(each_highlight.text)
    highlight_list.append(each_highlight.text.strip())
#print(highlights)
data = {"title":bookTitle.text.strip(),"author":author.text.strip(),"highlights":highlight_list}
print(data)
#json_data = json.dumps(data)

#print(json_data)
