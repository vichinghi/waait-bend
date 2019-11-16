from marshmallow import fields, ValidationError

from ..utils.base_schema import BaseSchema

from .models import Website


def validate_url(url):
    if Website.query.filter_by(url=url).all():
        raise ValidationError("Website with '{name}' already exists")


class WebsiteSchema(BaseSchema):
    url = fields.Url(validate=validate_url)

    class Meta:
        model = Website
