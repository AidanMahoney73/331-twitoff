# twitoff/routes/twitter_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from twitoff.models import db, Book, parse_records
from twitoff.services.twitter_service import api as twitter_api

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):

    # TODO: fetch user info
    user = twitter_api.get_user(screen_name)

    # TODO: fetch user tweets
    statuses = twitter_api.user_timeline("elonmusk", tweet_mode="extended",count=35, exclude_replies=True, include_rts=False)

    # TODO: fetch tweet embedding

    # TODO: store user info in db
    # TODO: store tweet and embedding in db

    # return f"Successfully fetched {screen_name}."
    return jsonify({"user": user._json, "num_tweets": len(statuses)})