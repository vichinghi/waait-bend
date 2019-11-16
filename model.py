import datetime
from routes import db


class IncidentReport(db.Model):
    __tablename__ = 'incident_reports'

    id = db.Column(db.Integer, primary_key=True)
    criminal = db.relationship('Criminal', backref='incident_report', lazy=True)
    what_happened = db.Column(db.String)
    how_it_happend = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    where_it_happend = db.Column(db.String)
    website = db.Column(db.String)
    url = db.Column(db.String)


class Criminal(db.Model):
    __tablename__ = 'criminals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)


class Website(db.Model):
    __tablename__ = 'websites'

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String)
