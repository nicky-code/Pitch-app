from flask import render_template,abort
from . import main
from flask_login import login_required
from ..models import User

# Views
# @main.route('/')
# def index():
    #....
 @main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@login_required   
    
