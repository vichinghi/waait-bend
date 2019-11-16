# -*- coding: utf-8 -*-
"""Rating views."""
from flask import Blueprint, jsonify, make_response, request
from flask.views import MethodView

from bs4 import BeautifulSoup
from urllib.request import urlopen


from nltk.text import TokenSearcher
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


blueprint = Blueprint("scraper", __name__, url_prefix="/scrape")


class ScrapeView(MethodView):
    def get(self):
        key_words = [
            "<Customs*>", "<seized>", "<seize>", "<confiscation>", "<confiscated>", "<confiscat>", "<wildlife>", "<seize>", "<confiscat>", "<ivory>", "<confiscat>", "<rhino>", "<confiscat>", "<pangolin>", "<elephant>", "<tusk>", "<rhino>", "<horn>", "<pangolin+scale>", "<illegal+wildlife+trade>", "<wildlife+trafficking>", "<hunting+trophies>", "<hunting+trophy>", "<endangered+species>", "<poaching>"
        ]
        joined_key_words = ''.join(key_words)
        web_sites = [
            'https://www.customs.gov.hk/en/publication_press/press/index_current.html',
            # 'https://customsnews.vn/',
            # 'https://www.apnews.com/'
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
        titles_links = []
        for x in sources:
            if x.find('table'):
                titles_links = [
                    {
                        'https://www.customs.gov.hk/en/publication_press/press' + a['href']: a['title']
                    } for a in x.findAll("table", {"class": "altbg"})[0].findAll("a")
                ]
                tables.append(
                    x.findAll('tbody')[0].findAll('tr')
                )


        # TODO
        # this doesn't work
        relevant_links = []
        for x in titles_links:
            tokenized_words = word_tokenize(x[[*x][0]])
            text = TokenSearcher(tokenized_words)
            key_words = text.findall(joined_key_words)
            if key_words:
                relevant_links.append({[*x][0]: x[[*x][0]]})

        print(relevant_links)
        return {"scraped": True}, 200


blueprint.add_url_rule("/", view_func=ScrapeView.as_view("scrape_websites"))
