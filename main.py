from bs4 import BeautifulSoup
import urllib.request

def get_headlines():
    r = urllib.request.urlopen("https://www.nytimes.com/")  # returns html of the website

    soup = BeautifulSoup(r, "html.parser") #parse html

    headlines = []

    links = soup.find_all('a') #find all code with tag a

    for link in links:
      headline = link.find('h3')
      if headline != None: 
        print(headline.text)
    return headlines
    
def get_links():

    r = urllib.request.urlopen("https://www.nytimes.com/")  # returns html of the website

    soup = BeautifulSoup(r, "html.parser") #parse html

    articles = []

    links = soup.find_all('')
  
    return articles
    
get_headlines()
#print(get_links())