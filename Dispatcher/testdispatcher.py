import pytest

from Dispatcher.dispatchrider import calculate_riders_wage
from Dispatcher.invaliderror import InvalidNumberOfDelivery


def test_calculate_riders_wages_for_25_delivery():
    assert calculate_riders_wage(25) == 9000


def test_calculate_riders_wages_for_80_delivery():
    assert calculate_riders_wage(80) == 45000


def test_calculate_riders_wages_for_60_delivery():
    assert calculate_riders_wage(60) == 20000


def test_calculate_riders_wages_for_70_delivery():
    assert calculate_riders_wage(70) == 40000


def test_calculate_riders_wages_above_raise_error():
    with pytest.raises(InvalidNumberOfDelivery) as info:
        calculate_riders_wage(188)
    assert str(info.value) == "number of delivery not within range"
