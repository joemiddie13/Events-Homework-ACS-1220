"""Create database models to represent tables."""

from events_app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Enum
from enum import Enum

guest_event_table = db.Table('guest_event_table',
  db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
  db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'), primary_key=True)
)

class Guest(db.Model):
  """Model representing a guest in the database."""
  __tablename__ = 'guest'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  phone = db.Column(db.String(20), nullable=False)
  events_attending = relationship('Event', secondary=guest_event_table, back_populates='guests')

class EventType(Enum):
  """Enumeration representing different types of events."""
  PARTY = "PARTY"
  STUDY = "STUDY"
  NETWORKING = "NETWORKING"

class Event(db.Model):
  """Model representing an event in the database."""
  __tablename__ = 'event'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(500), nullable=False)
  date_and_time = db.Column(db.DateTime, nullable=False)
  event_type = db.Column(db.Enum(*[e.value for e in EventType]), nullable=False)
  guests = relationship('Guest', secondary=guest_event_table, back_populates='events_attending')
