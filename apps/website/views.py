# -*- coding: utf-8 -*-
"""Rating views."""
from flask import Blueprint, jsonify, make_response, request, current_app
from flask.views import MethodView

from ..utils.view_utils import delete_by_id
from ..scraper import run_scraper
from .models import Website
from .schema import WebsiteSchema
from ..scheduler import scheduler

blueprint = Blueprint("Website", __name__, url_prefix="/website")


class WebsitesView(MethodView):
    def get(self):
        all_websites = Website.query.all()
        schema = WebsiteSchema(many=True)
        return {"websites": schema.dump(all_websites)}, 200

    def post(self):
        request_data = request.get_json()
        schema = WebsiteSchema()
        url = schema.load(request_data)
        url_string = schema.dump(url).get('url')
        run_scraper(url_string)
        url.save()
        return make_response(jsonify({"website": schema.dump(url)}), 201)


class WebsiteView(MethodView):
    def get(self, id):
        url = Website.get_or_404(id)
        schema = WebsiteSchema()
        return make_response(jsonify({"website": schema.dump(url)}), 200)

    def put(self, id):
        url = Website.get_or_404(id)
        request_data = request.get_json()
        schema = WebsiteSchema()
        url = schema.load(request_data, instance=url, partial=True)
        return make_response(jsonify({"website": schema.dump(url)}), 200)

    def delete(self, id):
        return delete_by_id(Website, id, "Wwbsite")


blueprint.add_url_rule("/", view_func=WebsitesView.as_view("many_websites"))
blueprint.add_url_rule("/<id>", view_func=WebsitesView.as_view("one_website"))
