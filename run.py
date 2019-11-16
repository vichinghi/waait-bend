# -*- coding: utf-8 -*-
"""Create an application instance."""
from apps.app import create_app
from bs4 import BeautifulSoup
from urllib.request import urlopen
from flask import Flask, request, jsonify, render_template

app = create_app()



@app.route('/')
def index():
    web_sites = [
        'https://www.customs.gov.hk/en/publication_press/press/index_current.html',
        'https://customsnews.vn/',
        'https://www.apnews.com/'
    ]
    sources = []
    print(web_sites)
    for v in web_sites:
        m_ = urlopen(v)
        n_ = BeautifulSoup(m_, 'html.parser')
        sources.append(
            n_
        )

    tables = []
    pages = []
    for x in sources:
        if x.find('tbody'):
            tables.append(
                x.find('tbody').get_text()
            )
        if not x.find('tbody'):
            pages.append(x.get_text())
    print(tables)
    print(pages)
    return render_template('index.html', **locals())
