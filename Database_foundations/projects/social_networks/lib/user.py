class User:
    def __init__(self,id,username,email) -> None:
        self.id = id
        self.username = username
        self.email = email
        
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
    def __repr__(self) -> str:
        return f"User({self.id}, {self.username}, {self.email})"