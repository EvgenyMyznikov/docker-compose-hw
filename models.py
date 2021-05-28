from datetime import datetime
from app import Base
import sqlalchemy as db


class Post(Base):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    owner = db.Column(db.String, nullable=False)
