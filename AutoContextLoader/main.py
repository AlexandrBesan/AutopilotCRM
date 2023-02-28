import requests
from bs4 import BeautifulSoup
 
def get_urls(page):
  """
  This function takes a webpage as an argument and returns a list of all the URLs that are linked to from that page.
  """
  response = requests.get(page , verify=False)
  html = response.content
  soup = BeautifulSoup(html, 'html.parser')
  links = {l.get('href'):l.get_text()  for l in soup.select("a[href*=http]")  }
  return links
 