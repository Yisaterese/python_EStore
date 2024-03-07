
from Dispatcher.dispatchrider import calculate_riders_wage


def test_calculate_riders_wages_for_25_delivery():
    assert calculate_riders_wage(25) == 9000