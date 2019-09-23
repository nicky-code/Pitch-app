from flask import render_template,request,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch , Category, Comment ,Votes
from .forms import UpdateProfile, PitchForm, CategoryForm, CommentForm
from .. import db,photos


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    category = Category.get_categories
    
    return render_template('index.html', category = category)

@main.route('/add/category', methods=['GET', 'POST'])
@login_required
def new_category():
    '''
    View new route function that returns a page with a form to create


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        
    return redirect(url_for('main.profile',uname=uname))
