# app/models/role.py
from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String
from typing import List

from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.user import User

from app.models.association import UserRole

class Role(db.Model):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    users: Mapped[List["User"]] = relationship(
        secondary=UserRole, back_populates="roles"
    )

    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, name={self.name!s})"