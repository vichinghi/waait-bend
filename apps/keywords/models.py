# -*- coding: utf-8 -*-
"""Location models."""
from ..database import db, Model, SurrogatePK


class Keyword(SurrogatePK, Model):

    __tablename__ = "keyword"
    word = db.Column(db.String(80), unique=True, nullable=False, index=True)

    def __init__(self, word, **kwargs):
        """Create instance."""
        db.Model.__init__(self, word=word, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<Keyword({self.word})>"
