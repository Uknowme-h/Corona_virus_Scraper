
import bs4;
import requests;


url = 'https://www.worldometers.info/coronavirus/'
source  = requests.get(url).text
soup = bs4.BeautifulSoup(source,'html.parser')

headings = [head.text.strip().replace('\n','') for head in soup.find_all('th')[1:15]]

def scrape(soup,headings):
    datas = soup.find_all('td');
    td_elements = [element.text for element in datas[176:]]


    row_data = []
    for i in range(0, len(td_elements), 22):  
      group = td_elements[i:i+22]  
      processed_group = []
      for element in group[:14]:  
        processed_group.append("N/A" if element == '' else element)  
        row_data.append(processed_group)  
    print("worked")
scrape(soup,headings);