# twitoff/__init__.py

from flask import Flask

from twitoff.models import db, migrate
from twitoff.routes.home_routes import home_routes
from twitoff.routes.book_routes import book_routes

DATABASE_URI = "sqlite:///D:\\School\\unit3\\sprint3\\331-twitoff\\twitoff_development.db"
SECRET_KEY = "super secret"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)