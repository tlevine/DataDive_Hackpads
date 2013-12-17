import os
import json

import nose.tools as n
import lxml.html

import hackpad_parser as h

source_html = lxml.html.fromstring(open(os.path.join('Fixtures','moda.html')).read())
expected = json.load(open(os.path.join('Fixtures','moda.json')))

def test_overview():
	observed = h.overview(source_html)
	print observed
	n.assert_equal(observed, expected['overview'])

def test_ngo_contacts():
	observed = h.contacts("NGO Representatives", source_html)
	n.assert_list_equal(list(observed), expected['contacts']['ngo'])

def test_challenges():
	observed = h.challenges(source_html)
	print observed
	n.assert_equal(observed, expected['challenges'])

