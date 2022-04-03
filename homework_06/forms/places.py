from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FloatField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError

from models import Place


class AddPlaceForm(FlaskForm):
    name_place = StringField('Название', validators=[InputRequired(), Length(5, 50)])
    description = TextAreaField('Детальное описание', validators=[InputRequired(), Length(100, 1550)])
    category = SelectField('Категория', coerce=int)
    city = SelectField('Город', coerce=int)
    rate = FloatField('Ваша оценка по 10 бальной шкале',
                      validators=[InputRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField('Создать')

    def validate_name_place(self, name_place):
        if Place.query.filter_by(name_place=name_place.data).first():
            raise ValidationError('Место с таким наванием уже существует')
