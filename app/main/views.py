from flask import render_template,request,url_for,abort,redirect
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch , Category, Comment 
from .forms import UpdateProfile, PitchForm, CategoryForm, CommentForm
from .. import db,photos


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    category = Category.get_categories()
    print(category)
    
    return render_template('index.html', category = category)

@main.route('/add/category', methods=['GET', 'POST'])
@login_required
def new_category():
    '''
    View new route function that returns a page with a form to create a category
    '''
    form = CategoryForm()
    
    if form.validate_on_submit():
        name = form.name.data
        new_category = Category(name=name)
        new_category.save_category()
        
        return redirect(url_for('.index'))
    
    title = 'New category'
    return render_template('new_category.html', category_form = form, title = title)
     
     
@main.route('/categories/<int:id>')
def category(id):
    # cat = Category.query.get(id)
    cat = Category.query.all()
    # pitches = Pitch.query.filter_by(category=cat.name).all()
    
    return render_template('category.html', category=cat)


@main.route('/categories/view_pitch/add/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    '''
    Function to check Pitches form and fetch data from the fields
    '''
    form = PitchForm()
    category = Category.query.filter_by(id=id).first()
    pitches = Pitch.query.filter_by(category=category.id).all()
    
    # if category is None:
    #     abort(404)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        post = form.post.data
        title= form.title.data
        new_pitch = Pitch(title=title, post=post, category=category.id, user_id =current_user.id )
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
  
    title = 'New Pitch'
    return render_template('new_pitch.html', title = title, pitch_form = form, category = category)

@main.route('/categories/view_pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):
    '''
    Function the returns a single pitch for comment to be added
    '''
    
    print(id)
    pitches = Pitch.query.get(id)
    
    if pitches is None:
        abort(404)
        
    comment = Comments.get_comments(id)
    return render_template('pitch.html', pitches=pitches, comment=comment, category_id=id)


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

    return render_template("profile/profile.html", user=user)


@main.route('/downvote/<int:id>', methods=['GET','POST'])
def downvotes(id):
    pitch = Pitch.query.filter_by(id=id).first()
    
    pitch.downvotes = pitch.downvotes +1
    
    db.session.add(pitch)
    db.session.commit()
    return redirect("/".format(id=pitch.id))


@main.route('/upvote/<int:id>', methods=['GET','POST'])
def upvotes(id):
    pitch = Pitch.query.filter_by(id=id).first()
    
    print(pitch)
    
    pitch.upvotes = pitch.upvotes +1
    
    db.session.add(pitch)
    db.session.commit()
    return redirect("/".format(id=pitch.id))
    return redirect(".profile".format(id=pitch.id))


@main.route('/new_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    Function that adds a comment
    '''
    form = CommentForm()
    comment = Comment.query.filter_by(pitch_id=id).all()
    pitches = Pitch.query.filter_by(id=id).first()
    user = User.query.filter_by(id=id).first()
    title =f'Welcome to Pitches Comments'
    
    if form.validate_on_submit():
        feedback = form.comment.data
        new_comment = Comment(feedback=feedback, user_id=current_user.id, pitch_id=pitches.id)
        new_comment.save_comment()
        
        return redirect(url_for('.index',uname=current_user.username))
    return render_template('comment.html',title=title, comment_form=form, pitches=pitches)
        