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
	'''
	<h2>
   Contacts
  </h2>
  <p>
   <b>
    NGO Representatives
   </b>
  </p>
  <ul>
   <li>
    Sohaib Hasan, MODA, shasan2@cityhall.nyc.gov
   </li>
   <li>
    Aida Shoydokova, MODA, analytics1@cityhall.nyc.gov
   </li>
  </ul>
  <p>
   <b>
    Data Ambassadors
   </b>
  </p>
  <ul>
	'''
	contacts = '//h2[contains(text(),"Contacts")]'
	ngo = '/following-sibling::p[b[contains(text(),"NGO Representatives")]]'
	people = '/following-sibling::ul[position()=1]/li/text()'
	print 88
	print html.xpath(contacts + ngo + people)
	return unidecode('')

if __name__ == '__main__':
	import json
	print json.dumps(parse('Fixtures/moda.html'))