from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    author = StringField(validators=[DataRequired()])
    submit = SubmitField('Add book')
