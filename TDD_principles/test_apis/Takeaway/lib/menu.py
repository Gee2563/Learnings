class Menu:
    def __init__(self) -> None:
        self.list = []
    
    def add_dish(self,dish):
        self.list.append(dish)

    def show_available_dishes(self):
        return [ f"{dish.name} : {dish.price}" for dish in self.list if dish.available == True]