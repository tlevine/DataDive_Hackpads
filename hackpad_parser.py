import lxml.html
from unidecode import unidecode

def overview(html):
	'Given an lxml HTML tree, extract the overview.'
	xpath = '//h2[position()=2]/following-sibling::p[position()=1]/text()'
	return unidecode(html.xpath(xpath)[0].strip())

def parse(filename):
	'Parse an HTML file from Hackpad.'
	raw_html = open(filename).read()
	html = lxml.html.fromstring(raw_html)
	return {
		"overview": overview(html),
	}

if __name__ == '__main__':
	import json
	print(json.dumps(
            parse('Fixtures/moda.html'),
            indent = 2, separators = (',', ': ')
        ))
