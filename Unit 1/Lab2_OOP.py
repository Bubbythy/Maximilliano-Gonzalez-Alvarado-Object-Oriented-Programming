class name:
    def __init__(self, name, email, age, password):
        self.name = name
        self.email = email
        self.age = age
        self.__password = password
    
def login(self):
    print(f"The user logs in with the email ({self.email}) and the password ({self.__password})")

class post:
    def __init__(self, author, comments, text):
        self.author = author
        self.comments = comments
        self.text = text
    def create_post(self):
        print(f"{self.author} posts {self.text}")




class comments:
    def __init__(self, author, comments, post):
        self.author = author
        self.comments = comments
        self.post = post
    def create_comment(self):
        print(f"{self.author} makes a comment under {self.post}")



class message:
    def __init__(self, author, receipient, text):
        self.author = author
        self.receipient = receipient
        self.text = text
    def send_message(self):
        print(f"{self.author} sends {self.text} to {self.receipient}")



post1 = post("mike2222", "1", "alabimbomban")
comments1 = comments("dierego", "0", "alabimbomban")
message1 = message("dierego", "maik2222", "bro deja de copiarme")

post1.create_post( )
comments1.create_comment( )
message1.send_message( )