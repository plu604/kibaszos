from application import app
from application.forms import NewGameForm
from flask import render_template, redirect, url_for, request

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/new_game", methods=["GET", "POST"])
def new_game():
    form = NewGameForm()
    if form.validate_on_submit():
        player1 = form.player1.data
        player2 = form.player2.data
        player3 = form.player3.data
        player4 = form.player4.data
        return redirect(url_for("scoreboard", player1=player1, player2=player2, player3=player3, player4=player4))
    return render_template("new_game.html", form=form)


@app.route("/scoreboard")
def scoreboard():
    player1 = request.args.get("player1")
    player2 = request.args.get("player2")
    player3 = request.args.get("player3")
    player4 = request.args.get("player4")
    return render_template("scoreboard.html", player1=player1, player2=player2, player3=player3, player4=player4)


@app.route("/rules")
def rules():
    return render_template("rules.html")


@app.route("/test")
def test():
    return render_template("test.html")