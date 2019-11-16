# -*- coding: utf-8 -*-
"""Create an application instance."""
from apps.app import create_app
from bs4 import BeautifulSoup
from urllib.request import urlopen
from flask import Flask, render_template


app = create_app()


source = urlopen('http://api.worldbank.org/v2/countries/AFG')
soup = BeautifulSoup(source, 'xml')


@app.route('/')
def index():
    web_sites = [
        'https://www.customs.gov.hk/en/publication_press/press/index_current.html',
        'https://customsnews.vn/',
        'https://www.apnews.com/'
    ]
    sources = []
    for i, v in enumerate(web_sites):
        exec('source_{}'.format(str(i))) = urlopen(v)
        exec('soup_{}'.format(str(i))) = BeautifulSoup(
            exec('source_{}'.format(str(i))), 'html.parser'
        )
        sources.append(
            exec('soup_{}'.format(str(i)))
        )

    tables = []
    for x in sources:
        tables.append(
            x.find('tbody').get_text()
        )
    print(tables)
    return render_template('index.html', **locals())
