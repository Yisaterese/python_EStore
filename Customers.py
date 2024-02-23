from Users import Users


class Customer(Users):
    def __init__(self, Billing_information, ShoppingCart):
        self.billing_information = Billing_information()
        self.shoppingCart = ShoppingCart()