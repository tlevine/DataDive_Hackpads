import nose.tools as n

import hackpad_parser as h

source_html = open(os.path.join('Fixtures','moda.html')).read()
expected = json.load(open(os.path.join('Fixtures','moda.json')))

def test_overview():
	observed = h.overview(source_html)
	n.assert_dict_equal(observed['overview'], expected['overview'])
