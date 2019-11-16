# -*- coding: utf-8 -*-
"""Location models."""
from ..database import db, Model, SurrogatePK
from datetime import datetime

class Criminal(SurrogatePK, Model):
    __tablename__ = 'criminals'

    name = db.Column(db.String)
    description = db.Column(db.String)


class Website(SurrogatePK, Model):
    __tablename__ = 'websites'

    link = db.Column(db.String)


class IncidentReport(SurrogatePK, Model):
    __tablename__ = 'incident_reports'

    what_happened = db.Column(db.String)
    how_it_happend = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    where_it_happend = db.Column(db.String)
    website = db.Column(db.String)
    url = db.Column(db.String)
    criminals = db.relationship('Criminal', lazy=True, secondary="criminal_incident_association",)


association_table = db.Table('criminal_incident_association',
                             db.Column('criminal', db.Integer, db.ForeignKey('criminals.id')),
                             db.Column('incident', db.Integer, db.ForeignKey('incident_reports.id'))
                             )
