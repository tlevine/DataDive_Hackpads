import lxml.html
from unidecode import unidecode

def overview(html):
	'Given an lxml HTML tree, extract the overview.'
	xpath = '//h2[contains(text(),"Overview")]/following-sibling::p[position()=1]/text()'
	return unidecode(html.xpath(xpath)[0].strip())

def parse(filename):
	'Parse an HTML file from Hackpad.'
	raw_html = open(filename).read()
	html = lxml.html.fromstring(raw_html)
	return {
		"overview": overview(html),
	}

def ngo_contacts(html):
	contacts = '//h2[contains(text(),"Contacts")]'
	ngo = '/following-sibling::p[b[contains(text(),"NGO Representatives")]]'
	people = '/following-sibling::ul[position()=1]/li/text()'
	
	people_text = html.xpath(contacts + ngo + people)
	keys = ['name','position','email address']
	for t in people_text:
		values = [part.strip() for part in t.split(',')]
		yield dict(zip(keys,values))

if __name__ == '__main__':
	import json
	print json.dumps(parse('Fixtures/moda.html'))