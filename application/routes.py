# File to include all routes to be used by the application.

from application import app
from application.forms import NewGameForm, RoundScores
from application.app_functions import store_new_game_data, save_scores, sum_validation, scoring_validation
from flask import render_template, redirect, url_for, request, session, flash


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
    if request.method =="POST":
        if scoring_validation(form.player1_score.data, form.player2_score.data, form.player3_score.data, form.player4_score.data):
            if sum_validation(form.player1_score.data, form.player2_score.data, form.player3_score.data, form.player4_score.data):
                save_scores(int(form.round_number.data), form.player1_score.data, form.player2_score.data, form.player3_score.data, form.player4_score.data)
                session.modified = True
                return render_template("scoreboard.html", form=form)
            else:
                flash("A pozitív pontok összege nem 40.", "Hiba")
                return render_template("scoreboard.html", form=form)
        else:
            flash("A pontszám 0 és 40 közötti, vagy -10 lehet!", "Hiba")
            return render_template("scoreboard.html", form=form)
    else:
        return render_template("scoreboard.html", form=form, edit_round=edit_round)


# Route for the "rules" page - to be added later
@app.route("/rules")
def rules():
    return render_template("rules.html")


# Route for "about"
@app.route("/about")
def about():
    return render_template("about.html")

# Test route - to be removed
@app.route("/test")
def test():
    return render_template("test.html")