from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

MY_DB = 'sqlite:///./app/db'

engine = create_engine(MY_DB, connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()

