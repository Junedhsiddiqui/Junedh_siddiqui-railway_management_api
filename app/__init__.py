from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config.Config')
db = SQLAlchemy(app)

from app.routes import admin_routes, user_routes
