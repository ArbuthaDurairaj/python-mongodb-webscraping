import requests
from bs4 import BeautifulSoup

# make a request to the site and get it as a string
markup = requests.get(f'http://quotes.toscrape.com/').text

# pass the string to a BeatifulSoup object
soup = BeautifulSoup(markup, 'html.parser')

#this will hold all the quotes
quotes_scrape = []

# now we can select elements
for item in soup.select('.quote'):
    quote = {}
    quote['text'] = item.select_one('.text').get_text()
    quote['author'] = item.select_one('.author').get_text()

    # get the tags element
    tags = item.select_one('.tags')

    # get each tag text from the tags element
    quote['tags'] = [tag.get_text() for tag in tags.select('.tag')]
    quotes_scrape.append(quote)
    
print(quotes_scrape)
