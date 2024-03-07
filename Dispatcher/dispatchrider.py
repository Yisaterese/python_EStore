from Dispatcher.invaliderror import InvalidNumberOfDelivery


def clculate_riders_wage(number_of_delivery):
    if number_of_delivery < 50:
        return number_of_delivery * 160 + 5000
    elif  number_of_delivery < 60:
        return number_of_delivery * 200 + 5000

    elif number_of_delivery < 70:
        return number_of_delivery * 250 + 5000
    elif number_of_delivery  >= 70:
        return number_of_delivery * 500 + 5000
    elif 1 > number_of_delivery > 100:
        raise InvalidNumberOfDelivery("number of delivery above range");
