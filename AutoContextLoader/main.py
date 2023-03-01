import requests
from bs4 import BeautifulSoup
 
def get_urls(url):
    """
    This function takes a webpage as an argument and returns a list of all the URLs that are linked to from that page.
    """
    response = requests.get(url , verify=False)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    links = {l.get('href'):l.get_text()  for l in soup.select("a[href*=http]")  }
    return links




def parse_page_info_pile(page):
    """
    This function parse all p, h and table content into list of strings
    """
    soup = BeautifulSoup(page.content, 'html.parser')
    p_tags = soup.find_all('p')
    h_tags = soup.find_all('h')

    data = []

    for tag in p_tags + h_tags:
        text = tag.get_text()
        if text:
            data.append(  text) 
 
    tables = soup.find_all('table') + soup.find_all('div', {'class': 'table'})
 
    for table in tables:
        table_data = []
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(['td', 'th'])
            row_data = []
            for cell in cells:
                cell_value = cell.get_text()
                row_data.append(cell_value)
            table_data.append(row_data)
        data.append(table_data) 

    return data

if __name__=='__main__': 
    print('get urls')
    urls = get_urls('https://pypi.org' )
    print(urls)
    print('get content')
    response = requests.get('https://pypi.org' , verify=False) 
    test = parse_page_info_pile(response)
    print(test)