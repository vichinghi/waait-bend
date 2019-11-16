from marshmallow import fields, ValidationError

from ..utils.base_schema import BaseSchema

from .models import Keyword


def validate_word(word):
    if Keyword.query.filter_by(word=word).all():
        raise ValidationError("Keyword '{name}' already exists")


class KeywordSchema(BaseSchema):
    word = fields.Str(validate=validate_word)

    class Meta:
        model = Keyword
