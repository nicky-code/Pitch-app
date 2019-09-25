from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# from app.models import User, Pitch, Category, Comment


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch')
    comments = db.relationship('Comment')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(80))
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        
    
    def __repr__(self):
        return f'User {self.username}'
        
        
    def save_user(self):
        User.all_users.append(self)
     
        
    @classmethod
    def clear_users(cls):
        User.all_users.clear()
    
    
        
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    post = db.Column(db.String(255))
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment')
    feedback = db.Column(db.String(255))
    upvotes = db.Column(db.Integer)
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()
        
    
    def get_pitches(id):
        pitches = Pitch.query.filter_by(category=id).all()
        return pitches
    
    @classmethod
    def count_pitches(cls,uname):
        user = User.query.filter_by(username=uname).first()
        pitches = Pitch.query.filter_by(user_id=user.id).all()
        
        pitches_count = 0
        for pitch in pitches:
            pitches_count += 1
            
        return pitches_count    
    
            
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    pitched = db.relationship('Pitch')
    
    
    def save_category(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories
        

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    feedback = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    votes = db.Column(db.Integer)
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(self,id):
        comment = Comments.query.filter_by(pitches_id = id).all()
        return comment
        
    
        
        
    
    
    
