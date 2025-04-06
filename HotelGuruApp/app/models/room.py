from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String
from typing import List, Optional

class Room(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    number: Mapped[str] = mapped_column(db.String(10), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)
    
    type: Mapped[str] = mapped_column(db.String(50), nullable=False)
    
    status: Mapped[str] = mapped_column(db.String(20), default="available")  # available, booked, maintenance
