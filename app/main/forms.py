from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, PasswordField, ValidationError, BooleanField, SelectField 
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
#Pitch Form
class PitchForm(FlaskForm):
    content = TextAreaField('Kindly post your Pitch')  
    submit = SubmitField('Submit Pitch')
    
    