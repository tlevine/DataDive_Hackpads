import lxml.html

def overview(raw_html):
	html = lxml.html.fromstring(raw_html)
	return html.cssselect('h2')[0].text_content()