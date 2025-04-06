from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String
from typing import List, Optional


class Booking(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    room_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    
    check_in: Mapped[str] = mapped_column(db.DateTime, nullable=False)
    check_out: Mapped[str] = mapped_column(db.DateTime, nullable=False)
    
    status: Mapped[str] = mapped_column(db.String(20), default="pending")  # pending, confirmed, canceled