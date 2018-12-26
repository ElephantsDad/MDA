from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class SubmitForm(FlaskForm):
    username = StringField('Никнейм:',
                            validators=[DataRequired(),Length(min=2, max=15)])
    submit = SubmitField('Начать игру')

class SendMessageForm(FlaskForm):
    message = StringField('Сообщение:', validators=[DataRequired(),Length(max=200)])
    submit = SubmitField('Отправить')
