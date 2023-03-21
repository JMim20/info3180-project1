from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class AddPrpertyForm(FlaskForm):
    pTitle= StringField('Property Title', validators=[InputRequired()])
    description= TextAreaField('Desctiption', validators=[InputRequired()])
    number_of_bedrooms=StringField ('No. of Rooms', validators=[InputRequired()])
    number_of_bathrooms=StringField ('No. of Bathrooms', validators=[InputRequired()])
    price= StringField('Price', validators=[InputRequired()])
    property_type= SelectField('Property Type', validators=[InputRequired()], choices=[(1,"House"), (2, "Apartment")])
    location= StringField('Location', validators=[InputRequired()])
    photo= FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'],'JPG OR PNG FILES ONLY!')])

