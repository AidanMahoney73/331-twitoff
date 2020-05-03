from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from twitoff.stats_models import load_model

stats_routes = Blueprint("stats_routes", __name__)

# TODO: accept input related to iris training data (x values)
@stats_routes.route('/stats/predict', methods=["POST"])
def twitoff_predict():    


    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]


    # TODO: Train a model

    # TODO: make and return a prediction