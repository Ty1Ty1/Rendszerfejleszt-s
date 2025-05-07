from app.extensions import Base
from sqlalchemy import Column, ForeignKey, Table

UserRole = Table(
    "userroles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("role_id", ForeignKey("roles.id"))
)