# Context: we're building a web scraper that fetches stories from Google News by extracting
# all the <item></item> tags from Google News' RSS feed. 
# We'll use BeautifulSoup module to parde Google News' XML 

import collections
import collections.abc
collections.Callable = collections.abc.Callable

import urllib.request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Scraper:
    # This method takes a website to scrape from as parameter
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        # The urlopen() function makes a request to a website and returns a Response object
        # that has its XML stored in it, 
        r = urllib.request.urlopen(self.site)
        # The function response.read() returns the XML from the Response object. All of the 
        # XML from the website is in the variable xml
        xml = r.read()
        # Create a new BeautifulSoup object with the xml obtained in the previous step 
        # as parameter
        parser = "html.parser"
        # The BeautifulSoup object parses the XML
        sp = BeautifulSoup(xml, parser)

        # Look for all the "item" tags
        for item in sp.find_all("item"):
            # Look for the "title" of those "item" tags
            title = item.find("title")
            if title is None:
                continue
            else:
                print("\n" + title.text)
    
news = "https://news.google.com/news/rss/headlines"
Scraper(news).scrape()