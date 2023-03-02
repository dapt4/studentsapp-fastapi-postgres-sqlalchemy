from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

host = os.environ.get('ENV_HOST')
port = os.environ.get('ENV_PORT')
database = os.environ.get('ENV_DATABASE')
user = os.environ.get('ENV_USER')
password = os.environ.get('ENV_PASSWORD')

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
