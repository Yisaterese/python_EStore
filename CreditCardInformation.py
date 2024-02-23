class CreditCardInformation:
    def __init__(self, card_cvv:str, card_expiration_year:str, card_expiration_moth:str, credit_card_number:str, name_on_card:str, CardType):
        self.card_cvv = card_cvv
        self.card_expiration_year = card_expiration_year
        self.card_expiration_moth = card_expiration_moth
        self.credit_card_number = credit_card_number
        self.name_on_card = name_on_card
        self.cardType = CardType()