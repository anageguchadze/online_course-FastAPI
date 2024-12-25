from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.depends import get_db
from app.database import engine
from typing import List
from app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session=Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user

@app.post("/login/", response_model=schemas.User)
def login_user(username: str, password: str, db: Session=Depends(get_db)):
    user = crud.login_user(db, username, password)
    if not user:
        raise HTTPException(status_code=400, detail='Invalid Credentials')
    return user

@app.get("/userss/", response_model=schemas.User)
def read_user(user_id: int, db: Session=Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User Not Found!')
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session=Depends(get_db)):
    users = crud.get_user(db, skip=skip, limi=limit)
    return users