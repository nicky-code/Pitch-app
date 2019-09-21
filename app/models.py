

class User:
    '''
    User class to define User Objects
    '''
    
    def __init__(self,id,username,email,password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        
        
    def save_user(self):
        User.all_users.append(self)
     
        
    @classmethod
    def clear_users(cls):
        User.all_users.clear()
    
    
        
class Pitch:
    '''
    Pitch class to define Pitch Objects
    '''
    
    def __init__(self,id,category,content,upVotes,downVotes,publishedAt):
        self.id = id
        self.category = category
        self.content = content
        self.upVotes= upVotes
        self.downVotes = downVotes
        self.publishedAt = publishedAt
        
        
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
    
    def __init__(self,id,user-id,pitch-id,comment,feedback):
        self.id = id
        self.user-id = user-id
        self.pitch-id = pitch-id
        self.comment = comment
        self.feedback = feedback
        
        
class Votes:
    '''
    Votes class to define Votes Objects
    '''
    
    def __init__(self,id,user-id,pitch-id,upVotes,downVotes):
        self.id = id
        self.user-id = user-id
        self.pitch-id = pitch-id
        self.upVotes = upVotes
        self.downVotes = downVotes
        
        
        
        
    
    
    
