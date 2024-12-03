class Coffee:
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type

    def make_coffee(self):
        return f"{self.coffee_type} is ready!"
