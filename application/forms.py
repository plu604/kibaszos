# File for collecting all forms which may be used in the application.

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired

# Initial form to record player names for the game.
class NewGameForm(FlaskForm):
    player1 = StringField("Első játékos (kezd):", validators=[DataRequired()])
    player2 = StringField("Második játékos:", validators=[DataRequired()])
    player3 = StringField("Harmadik játékos:", validators=[DataRequired()])
    player4 = StringField("Negyedik játékos:", validators=[DataRequired()])
    submit = SubmitField("Kezdés!")

class RoundScores(FlaskForm):
    # TODO custom validator should be added to see if the total entered positive scores summed up is 40.
    round_number = HiddenField()
    player1_score = IntegerField("Első játékos pontszáma:", validators=[DataRequired()])
    player2_score = IntegerField("Második játékos pontszáma:", validators=[DataRequired()])
    player3_score = IntegerField("Harmadik játékos pontszáma:", validators=[DataRequired()])
    player4_score = IntegerField("Negyedik játékos pontszáma:", validators=[DataRequired()])
    submit = SubmitField("Mentés")