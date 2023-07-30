from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:devs@localhost/flask_migration'
app.config['SQLALCHEMY_TRACK_MODIFICATINS'] = False

app.app_context().push()

db = SQLAlchemy(app)
migrate = Migrate(app, db)
