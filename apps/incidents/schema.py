from marshmallow import fields, ValidationError, Schema

from ..utils.base_schema import BaseSchema

from .models import IncidentReport, Website, Criminal


class CriminalSchema(BaseSchema):
    class Meta:
        model = Criminal


class IncidentReportSchema(BaseSchema):
    criminals = fields.Nested(CriminalSchema, many=True)

    class Meta:
        model = IncidentReport


class IncidentReportArgs(Schema):
    what_happened = fields.Str()
    how_it_happend = fields.Str()
    date = fields.Date()
    where_it_happend = fields.Str()
    website = fields.Str()
    url = fields.Str()
