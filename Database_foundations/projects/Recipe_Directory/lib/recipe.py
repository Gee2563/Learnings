class Recipe:
    def __init__(self,id,name, cooking_time, rating) -> None:
        self.name  = name
        self.cooking_time = cooking_time
        self.rating = rating
        self.id = id
    

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__

    def __repr__(self) -> str:
        return f'Recipe({self.id}, {self.name}, {self.cooking_time}, {self.rating})'