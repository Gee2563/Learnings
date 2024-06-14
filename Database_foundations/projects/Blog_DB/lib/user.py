class User:
    def __init__(self,id, email, username,posts=[]) -> None:
        self.id = id
        self.email = email
        self.username = username
        self.posts = posts
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__  == value.__dict__
    def __repr__(self) -> str:
        return f'User({self.id}, {self.email}, {self.username}, {self.posts})'