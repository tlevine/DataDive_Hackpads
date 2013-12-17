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
		"contacts": {
			'ngo': list(contacts('NGO Representatives', html)),
			'data_ambassadors': list(contacts('Data Ambassadors', html)),
			'volunteers': list(contacts('Volunteers', html)),
		},
		"challenges": challenges(html),

	}

def contacts(section, html):
	contacts = '//h2[contains(text(),"Contacts")]'
	group = '/following-sibling::p[b[contains(text(),"' + section + '")]]'
	people = '/following-sibling::ul[position()=1]/li/text()'

	people_text = html.xpath(contacts + group + people)
	keys = ['name','position','email address']
	for t in people_text:
		values = [part.strip() for part in t.split(',')]
		yield dict(zip(keys,values))

def challenges(html):
	xpath = u'//h2[contains(text(),"The Challenge(s)")]/following-sibling::*'
	siblings = html.xpath(xpath)
	challenges = u''
	for sibling in siblings:
		if sibling.tag == 'h2':
			break
		else:
			challenges += lxml.html.tostring(sibling)
	return challenges


if __name__ == '__main__':
	import json
	print json.dumps(parse('Fixtures/moda.html'))