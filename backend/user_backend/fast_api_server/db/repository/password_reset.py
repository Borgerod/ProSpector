import secrets
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.password_reset import PasswordReset

# Long enough to open the email and type the code, short enough to limit guessing time
CODE_EXPIRE_MINUTES = 15
# With a 6-digit code, 5 tries give a 5 in 1,000,000 chance of guessing right
MAX_ATTEMPTS = 5


def create_reset_code(email: str, db: Session) -> str:
    ''' Stores a fresh code for email (replacing any older one) and returns it. '''
    code = f"{secrets.randbelow(1_000_000):06d}"
    reset = db.get(PasswordReset, email) or PasswordReset(email = email)
    reset.code_hash = Hasher.get_password_hash(code)
    reset.expires_at = datetime.now(timezone.utc) + timedelta(minutes = CODE_EXPIRE_MINUTES)
    reset.attempts = 0
    db.add(reset)
    db.commit()
    return code


def use_reset_code(email: str, code: str, db: Session) -> bool:
    ''' True if code is valid for email. A valid code works once. '''
    reset = db.get(PasswordReset, email)
    if reset is None:
        return False
    if reset.expires_at < datetime.now(timezone.utc) or reset.attempts >= MAX_ATTEMPTS:
        db.delete(reset)
        db.commit()
        return False
    if not Hasher.verify_password(code, reset.code_hash):
        reset.attempts += 1
        db.commit()
        return False
    db.delete(reset)
    db.commit()
    return True
