from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, MetaData, text, Enum
from sqlalchemy.orm import declarative_base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import enum

db= SQLAlchemy()

class BannedEmail (db.Model):
    #id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    #id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120),unique=True, nullable=False)
    app_uuid =db.Column(db.String(120))
    blocked_reason=db.Column(db.String(255))
    #Pending check this IP request
    request_ip=db.Column(db.String(120))
    #request Date and Time
    createdAt=db.Column(db.DateTime, default=datetime.utcnow)

class BannedEmailSchema(SQLAlchemyAutoSchema):
    id = fields.Integer()
    email = fields.String()
    app_uuid = fields.String()
    blocked_reason = fields.String()
    request_ip = fields.String()
    createdAt = fields.String()

    class Meta:
        model = BannedEmail
        load_instance = True

    data = fields.Raw(load_only=True)
