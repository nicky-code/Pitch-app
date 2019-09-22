from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    
    pass_secure = db.Column(db.String(255))
    
    
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
    
    
        
class Pitch:
    '''
    Pitch class to define Pitch Objects
    '''
    
    def __init__(self,id,category,post,upVotes,downVotes):
        self.id = id
        self.category = category
        self.post = post
        self.upVotes= upVotes
        self.downVotes = downVotes
        
        
        
class Category:
    '''
    Category class to define Category Objects
    '''
    
    def __init__(self,id,name):
        self.id = id
        self.name = name
        

class Comment:
    '''
    Comment class to define Comment Objects
    '''
    
    def __init__(self,id,user_id,pitch_id,comment,feedback):
        self.id = id
        self.user_id = user_id
        self.pitch_id = pitch_id
        self.comment = comment
        self.feedback = feedback
        
        
class Votes:
    '''
    Votes class to define Votes Objects
    '''
    
    def __init__(self,id,user_id,pitch_id,upVotes,downVotes):
        self.id = id
        self.user_id = user_id
        self.pitch_id = pitch_id
        self.upVotes = upVotes
        self.downVotes = downVotes
        
        
        
        
    
    
    
