from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class AddPrpertyForm(FlaskForm):
    pTile= StringField('Property Title', validators=[InputRequired()])
    description= TextAreaField('Desctiption', validators=[InputRequired()])
    numBedrooms=StringField ('No. of Rooms', validators=[InputRequired()])
    numBathrooms=StringField ('No. of Bathrooms', validators=[InputRequired()])
    price= StringFieldd('Price', validators=[InputRequired()])
    pType= SelectField('Property Type', validators=[InputRequired()], choices=[(1,"House"), (2, "Apartment")])
    location= StringField('Location', validators=[InputRequired()])
    photo= FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'],'JPG OR PNG FILES ONLY!')])

