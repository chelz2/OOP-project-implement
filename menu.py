class MenuItem:
    """"models each menu items"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water' : water,
            'milk' : milk,
            'coffee' : coffee,
        }

class Menu:
    """models the menu with drinks"""
    def __init__(self):
        self.menu = [
            MenuItem(name = "latte", cost = 2.5, water = 200, milk = 100, coffee = 10 ),
            MenuItem(name = "espresso", cost = 1.5, water = 200, milk = 100, coffee = 10 ),
            MenuItem(name = "cappucino", cost = 3, water = 200, milk = 100, coffee = 10 ),
        ]

    def get_items(self):
        """Returns the name of all the available items in Menu """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """searches for the drink by particular name, returns it if it exist otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("sorry that item is not available")
        


