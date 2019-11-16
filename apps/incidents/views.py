# -*- coding: utf-8 -*-
"""Rating views."""
from flask import Blueprint, jsonify, make_response, request
from flask.views import MethodView
from ..database import db

from ..utils.view_utils import delete_by_id
from .models import IncidentReport, Website, Criminal
from .schema import IncidentReportSchema, IncidentReportArgs
from webargs.flaskparser import use_args, use_kwargs

blueprint = Blueprint("incident", __name__, url_prefix="/incident")


class IncidentReportsView(MethodView):
    @use_args(IncidentReportArgs())
    def get(self, argument):
        all_incidents = IncidentReport.query.filter_by(**argument).all()
        schema = IncidentReportSchema(many=True)
        return {"incidents": schema.dump(all_incidents)}, 200

    def post(self):
        request_data = request.get_json()
        schema = IncidentReportSchema()
        incident = schema.load(request_data, transient=True)
        incident.save()
        return make_response(jsonify({"incidents": schema.dump(incident)}), 201)


class IncidentReportView(MethodView):
    def get(self, id):
        incident = IncidentReport.get_or_404(id)
        schema = IncidentReportSchema()
        return make_response(jsonify({"incident": schema.dump(incident)}), 200)

    def put(self, id):
        incident = IncidentReport.get_or_404(id)
        request_data = request.get_json()
        schema = IncidentReportSchema()
        incident = schema.load(request_data, instance=incident, partial=True)
        return make_response(jsonify({"incident": schema.dump(incident)}), 200)

    def delete(self, id):
        return delete_by_id(IncidentReport, id, "incident")


blueprint.add_url_rule("/", view_func=IncidentReportsView.as_view("incidents"))
blueprint.add_url_rule("/<id>", view_func=IncidentReportView.as_view("incident"))
