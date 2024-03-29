from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, PasswordField, ValidationError, BooleanField, SelectField,RadioField 
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
    
#Pitch Form
class PitchForm(FlaskForm):
    title=StringField('Add your title pitch')
    post = TextAreaField('Kindly post your Pitch')  
    submit = SubmitField('Submit Pitch')
    # vote = RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    
#Category Form
class CategoryForm(FlaskForm):
    name = TextAreaField('Category')
    submit = SubmitField()
    
    
#Comment Form
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()
    vote = RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    
    
    