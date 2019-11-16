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

    head = soup.find('wb:name').get_text()
    second_author = soup.find('wb:region').get_text()
    first_article = soup.find('wb:incomeLevel').get_text()
    print(head, second_author, first_article)
    return render_template('index.html', **locals())
