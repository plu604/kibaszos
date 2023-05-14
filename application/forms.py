from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewGameForm(FlaskForm):
    player1 = StringField("Első játékos (kezd):", validators=[DataRequired()])
    player2 = StringField("Második játékos:", validators=[DataRequired()])
    player3 = StringField("Harmadik játékos:", validators=[DataRequired()])
    player4 = StringField("Negyedik játékos:", validators=[DataRequired()])
    submit = SubmitField("Kezdés!")