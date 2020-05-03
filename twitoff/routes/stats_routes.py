from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from flask import Blueprint, jsonify, request, render_template, flash, redirect

stats_routes = Blueprint("stats_routes", __name__)

# TODO: accept input related to iris training data (x values)
@stats_routes.route('/stats/iris')
def iris():    
    x, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
    clf.fit(x, y)
    result = str(clf.predict(x[:2, :]))
    return result # TODO: return as JSON

    