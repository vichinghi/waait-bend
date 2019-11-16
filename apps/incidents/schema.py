from marshmallow import fields, ValidationError

from ..utils.base_schema import BaseSchema

from .models import IncidentReport, Website, Criminal


class CriminalSchema(BaseSchema):
    class Meta:
        model = Criminal


class IncidentReportSchema(BaseSchema):
    criminals = fields.Nested(CriminalSchema, many=True)

    class Meta:
        model = IncidentReport
