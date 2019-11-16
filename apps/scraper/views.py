# -*- coding: utf-8 -*-
"""Rating views."""
from datetime import datetime

from flask import Blueprint, jsonify, make_response, request
from flask.views import MethodView

from bs4 import BeautifulSoup
from urllib.request import urlopen


from ..fuzzy_text_analyzer import get_match, keys

from ..keywords.models import Keyword

from ..incidents.models import IncidentReport

blueprint = Blueprint("scraper", __name__, url_prefix="/scrape")


class ScrapeView(MethodView):
    def get(self):
        web_sites = [
            'https://www.customs.gov.hk/en/publication_press/press/index_current.html',
            # 'https://customsnews.vn/',
            # 'https://www.apnews.com/'
        ]
        sources = []
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
                        'https://www.customs.gov.hk' + a['href']: a['title']
                    } for a in x.findAll("table", {"class": "altbg"})[0].findAll("a")
                ]
                tables.append(
                    x.findAll('tbody')[0].findAll('tr')
                )

        relevant_links = list(filter(lambda x: get_match(x[[*x][0]]), titles_links))

        each_sites_data = []
        for v in relevant_links:
            m_ = urlopen([*v][0])
            n_ = BeautifulSoup(m_, 'html.parser')
            incident = IncidentReport(
                what_happened=v[[*v][0]],
                how_it_happend=n_.find(
                    'div', {'id': 'content_area'}
                ).find('p').text,
                date=datetime.now(),
                where_it_happend='Hong Kong',
                website=[*v][0],
                url=[*v][0],
                criminals=[]
            )
            incident.save()
        return {"scraped": True}, 200


blueprint.add_url_rule("/", view_func=ScrapeView.as_view("scrape_websites"))
