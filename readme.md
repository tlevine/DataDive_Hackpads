Parse [Hackpads]() from
[DataKind](http://datakind.org) data dives
into a structured format.

Install like so.

    pip install datadive_hackpads

Use it like so.

    import datadive_hackpads
    datadive_hackpads.download(url)
    datadive_hackpads.parse(file)

Run tests with nose.

    nosetests

We attempt to have this working on both Python 2.7 and Python 3.3.
