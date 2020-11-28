from flask import Flask
from api.route import auth_controller
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:joker@localhost:5432/graneros_db"
db = SQLAlchemy(app)

migrate = Migrate(app, db)

app.register_blueprint(auth_controller)

if __name__ == '__main__':
    app.run()
