# -*- coding: utf-8 -*-
"""Location models."""
from ..database import db, Model, SurrogatePK


class Website(SurrogatePK, Model):
    """A Location location.

    e.g Lagos, Kampala, Accra, New York
    """

    __tablename__ = "website"
    url = db.Column(db.String(80), unique=True, nullable=False, index=True)

    def __init__(self, url, **kwargs):
        """Create instance."""
        db.Model.__init__(self, url=url, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<Website({self.url})>"
