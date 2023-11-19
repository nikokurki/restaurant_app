from app import app
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from os.path import join, dirname


app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)
