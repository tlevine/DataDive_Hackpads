#!/usr/local/bin/python
import requests
from oauth_hook import OAuthHook
from bs4 import BeautifulSoup

consumer_key = 'vUVuFi9TB3j'
consumer_secret = 'vcnIcyyr293RxNpecwOuiqZ3fsbIFhho'

OAuthHook.consumer_key = consumer_key
OAuthHook.consumer_secret = consumer_secret
# self.oauth_hook = OAuthHook(header_auth=True)
oauth_hook = OAuthHook(header_auth=True)

pad_id = '5nsaXEL0jOv'
base_url = 'https://nycdatadive2013.hackpad.com'
path = '/api/1.0/pad/%s/content.html' % pad_id
url = base_url + path
        
request = requests.Request('GET', url)
# request = self.oauth_hook(request)
request = oauth_hook(request)
prepared = request.prepare()
        
session = requests.session()
resp = session.send(prepared)
page = resp.text
soup = BeautifulSoup(page)

# print page
# print soup.prettify()

headings = soup.find_all('h2')
# for thing in headings:
# 	print thing

print headings[2]
print soup.find_all('h2').b