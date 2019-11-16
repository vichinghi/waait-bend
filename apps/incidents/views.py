# -*- coding: utf-8 -*-
"""Rating views."""
from flask import Blueprint, jsonify, make_response, request
from flask.views import MethodView

from ..utils.view_utils import delete_by_id
from .models import IncidentReport, Website, Criminal
from .schema import IncidentReportSchema

blueprint = Blueprint("incident", __name__, url_prefix="/incident")


class IncidentReportsView(MethodView):
    def get(self):
        all_cities = IncidentReport.query.all()
        schema = IncidentReportSchema(many=True)
        return {"incidents": schema.dump(all_cities)}, 200

    def post(self):
        request_data = request.get_json()
        schema = IncidentReportSchema()
        city = schema.load(request_data)
        city.save()
        return make_response(jsonify({"incidents": schema.dump(city)}), 201)


class IncidentReportView(MethodView):
    def get(self, id):
        city = Website.get_or_404(id)
        schema = IncidentReportSchema()
        return make_response(jsonify({"incident": schema.dump(city)}), 200)

    def put(self, id):
        city = IncidentReport.get_or_404(id)
        request_data = request.get_json()
        schema = IncidentReportSchema()
        city = schema.load(request_data, instance=city, partial=True)
        return make_response(jsonify({"incident": schema.dump(city)}), 200)

    def delete(self, id):
        return delete_by_id(IncidentReport, id, "incident")


blueprint.add_url_rule("/", view_func=IncidentReportsView.as_view("incidents"))
blueprint.add_url_rule("/<id>", view_func=IncidentReportView.as_view("incident"))
