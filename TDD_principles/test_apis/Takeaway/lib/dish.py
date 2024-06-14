class Dish:
    def __init__(self,name,price) -> None:
        if type(name) == str and type(price) == int:
            self.name = name
            self.price = price
            self.available = True
        else:
            raise Exception('Invalid input')
        
    def set_unavailable(self):
        self.available = False

    
    def set_available(self):
        self.available = True