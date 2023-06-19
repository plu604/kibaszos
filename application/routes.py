# File to include all routes to be used by the application.

from application import app
from application.forms import NewGameForm, RoundScores
from application.app_functions import store_new_game_data, save_scores
from flask import render_template, redirect, url_for, request, session


# Route for the landing page (index)
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# Route to start a new game, entering player names
@app.route("/new_game", methods=["GET", "POST"])
def new_game():
    form = NewGameForm()
    if form.validate_on_submit():
        # Storing the form data in a session cookie
        store_new_game_data(form.player1.data, form.player2.data, form.player3.data, form.player4.data)
        return redirect(url_for("scoreboard"))
    return render_template("new_game.html", form=form)


# Redirect route for the scoreboard
@app.route("/scoreboard", methods=["GET", "POST"])
def scoreboard():
    form = RoundScores()
    edit_round = int(request.args.get("edit_round")) if request.args.get("edit_round") else None
    print(form.round_number.data)
    if form.validate_on_submit():
        save_scores(form.round_number.data, form.player1_score.data, form.player2_score.data, form.player3_score.data, form.player4_score.data)
        # I have no idea why this doesn't work properly
        if edit_round != form.round_number.data and form.round_number.data is not None:
            session["current_round"] += 1
        return render_template("scoreboard.html", form=form)
    return render_template("scoreboard.html", form=form, edit_round=edit_round)


# Route for the "rules" page - to be added later
@app.route("/rules")
def rules():
    return render_template("rules.html")


# Test route - to be removed
@app.route("/test")
def test():
    return render_template("test.html")