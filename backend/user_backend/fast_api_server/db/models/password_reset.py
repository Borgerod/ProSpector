from sqlalchemy import Column, DateTime, Integer, String
from db.base_class import Base


class PasswordReset(Base):
	''' One pending reset code per email. The code itself is only stored hashed. '''
	__tablename__ = "password_reset"
	email = Column(String, primary_key=True)
	code_hash = Column(String, nullable=False)
	expires_at = Column(DateTime(timezone=True), nullable=False)
	attempts = Column(Integer, nullable=False, default=0)
