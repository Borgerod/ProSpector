from core.hashing import Hasher
from db.models.users import User
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username = user.brukernavn,
        email = user.epost,
        hashed_password = Hasher.get_password_hash(user.passord),
        is_active = True,
        is_superuser = False,
        org = user.organisasjon
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()

def changePassword(new_password: str, email: str, db: Session):
    user = get_user_by_email(email, db)
    new_hash = Hasher().get_password_hash(new_password)
    user.hashed_password = new_hash
    db.commit()  
    return 'Success'

