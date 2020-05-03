# twitoff/routes/twitter_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from twitoff.models import db, User, Tweet, parse_records
from twitoff.services.twitter_service import api as twitter_api
from twitoff.services.basilica_service import connection as basilica_connection

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):

    #
    # fetch user info
    #

    user = twitter_api.get_user(screen_name)

    #
    # store user info in db
    #

    db_user = User.query.get(user.id) or User(id=user.id)

    db_user.screen_name = user.screen_name
    db_user.name = user.name
    db_user.location = user.location
    db_user.followers_count = user.followers_count

    db.session.add(db_user)
    db.session.commit()

    #
    # fetch user tweets
    #

    statuses = twitter_api.user_timeline("elonmusk", tweet_mode="extended",count=100, exclude_replies=True, include_rts=False)
 
    #
    # fetch tweet embeddings
    #

    tweet_texts = [status.full_text for status in statuses]
    embeddings = list(basilica_connection.embed_sentences(tweet_texts, model="twitter"))

    # 
    # TODO: store tweets in db with embedding
    #

    for index, status in enumerate(statuses):

        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.full_text = status.full_text

        embedding = embeddings[index]
        db_tweet.embedding = embedding

        db.session.add(db_tweet)
    db.session.commit()

    return f"Successfully fetched {screen_name}."
    # return jsonify({"user": user._json, "num_tweets": len(statuses)})