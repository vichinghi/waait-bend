from marshmallow import fields, ValidationError

from ..utils.base_schema import BaseSchema

from .models import IncidentReport, Website, Criminal


class IncidentReportSchema(BaseSchema):

    class Meta:
        model = IncidentReport
