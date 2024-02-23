from CreditCardInformation import CreditCardInformation


class Billing_information:
    def __init__(self,receiver_phone_number:str, receiver_name:str, delivery_address:str):
        self.receiver_phone_number = receiver_phone_number
        self.receiver_name = receiver_name
        self.delivery_address = delivery_address
        self.creditCardInfo = CreditCardInformation()