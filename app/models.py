from . import db


class User(db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    
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
        
        
        
        
    
    
    
