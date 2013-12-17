import lxml.html
from unidecode import unidecode

def overview(raw_html):
	html = lxml.html.fromstring(raw_html)
	xpath = '//h2[position()=2]/following-sibling::p[position()=1]/text()'
	return unidecode(html.xpath(xpath)[0].strip())