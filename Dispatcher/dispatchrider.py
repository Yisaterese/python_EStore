from Dispatcher.invaliderror import InvalidNumberOfDelivery


def calculate_riders_wage(number_of_delivery: int):
    if number_of_delivery < 1 or number_of_delivery > 100:
        raise InvalidNumberOfDelivery("number of delivery not within range")
    elif number_of_delivery < 50:
        return number_of_delivery * 160 + 5000
    elif number_of_delivery < 60:
        return number_of_delivery * 200 + 5000
    elif number_of_delivery < 70:
        return number_of_delivery * 250 + 5000
    elif number_of_delivery >= 70:

        return number_of_delivery * 500 + 5000
