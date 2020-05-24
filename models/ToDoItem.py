import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ToDoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False, default="pending")
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
