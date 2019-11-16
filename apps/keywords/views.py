# -*- coding: utf-8 -*-
"""Rating views."""
from flask import Blueprint, jsonify, make_response, request
from flask.views import MethodView

from ..utils.view_utils import delete_by_id
from .models import Keyword
from .schema import KeywordSchema

blueprint = Blueprint("Keyword", __name__, url_prefix="/keyword")


class KeywordsView(MethodView):
    def get(self):
        all_keywords = Keyword.query.all()
        schema = KeywordSchema(many=True)
        return {"keywords": schema.dump(all_keywords)}, 200

    def post(self):
        request_data = request.get_json()
        schema = KeywordSchema()
        word = schema.load(request_data)
        word.save()
        return make_response(jsonify({"keyword": schema.dump(word)}), 201)


class KeywordView(MethodView):
    def get(self, id):
        word = Keyword.get_or_404(id)
        schema = KeywordSchema()
        return make_response(jsonify({"keyword": schema.dump(word)}), 200)

    def put(self, id):
        word = Keyword.get_or_404(id)
        request_data = request.get_json()
        schema = KeywordSchema()
        word = schema.load(request_data, instance=word, partial=True)
        return make_response(jsonify({"keyword": schema.dump(word)}), 200)

    def delete(self, id):
        return delete_by_id(Keyword, id, "Keyword")


blueprint.add_url_rule("/", view_func=KeywordsView.as_view("many_keywords"))
blueprint.add_url_rule("/<id>", view_func=KeywordView.as_view("one_keyword"))
