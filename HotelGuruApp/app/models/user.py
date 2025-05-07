# app/models/user.py
from app.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String
from typing import List, Optional
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.association import UserRole 

from typing import List, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.role import Role
    
from typing import List, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.role import Address

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    phone : Mapped[str] = mapped_column(String(30))

    roles: Mapped[List["Role"]] = relationship(
        secondary=UserRole, back_populates="users"
    )

    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"))
    address : Mapped["Address"] = relationship(back_populates="user", lazy=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!s}, email={self.email!r})"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)