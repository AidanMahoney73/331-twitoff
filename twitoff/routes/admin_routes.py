# twitoff/routes/admin_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from twitoff.models import db

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route("/admin/db/reset")
def reset_db():
    print(type(db))
    db.drop_all()
    db.create_all()
    return f"The database has been reset"