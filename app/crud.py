from sqlalchemy.orm import Session
from app import models, schemas
from app.util import encrypt_password, check_password

def login_user(db: Session, username: str, password: str):
    username = db.query(models.User).filter(models.User.username == username).first()
    if not username:
        return None
    if not check_password(password, username.hashed_password):
        return None
    return username

    
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = encrypt_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
