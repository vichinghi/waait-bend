from flask import Flask, render_template
from bs4 import BeautifulSoup
from urllib.request import urlopen

# to run app ==> flask run


source = urlopen('http://api.worldbank.org/v2/countries/AFG')
soup = BeautifulSoup(source, 'xml')

app = Flask(__name__)


@app.route('/')
def index():

    head = soup.find('wb:name').get_text()
    second_author =  soup.find('wb:region').get_text()
    first_article = soup.find('wb:incomeLevel').get_text()
    print(head, second_author, first_article)
    return render_template('index.html', **locals())
