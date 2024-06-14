class Order:
    def __init__(self) -> None:
        self.list = []
        self.total_price = 0

    
    def add_dish(self, dish):
        self.list.append(dish)
        self.total_price += dish.price

    def remove_dish(self,dish):
        self.list.remove(dish)

    def view_order(self):
        return [f"{dish.name} : {dish.price}" for dish in self.list]