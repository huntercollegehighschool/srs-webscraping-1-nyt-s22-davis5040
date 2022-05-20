from bs4 import BeautifulSoup
import urllib.request

def get_headlines():
    r = urllib.request.urlopen("https://www.nytimes.com/")  # returns html of the website

    soup = BeautifulSoup(r, "html.parser") #parse html

    headlines = []

    return headlines
    
def get_links():

    r = urllib.request.urlopen("https://www.nytimes.com/")  # returns html of the website

    soup = BeautifulSoup(r, "html.parser") #parse html

    articles = []

    return articles
    
#print(get_headlines())
print(get_links())