class Order:
    def __init__(self):
        self.current_order = None

    def take_order(self, coffee_type):
        self.current_order = Coffee(coffee_type)

    def serve(self, customer):
        if self.current_order and self.current_order.coffee_type == customer.order:
            customer.served = True
            self.current_order = None
            return "Served!"
        return "Wrong order!"