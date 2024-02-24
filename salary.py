from decimal import Decimal
from employee import CommissionEmployee
from valueError import InvalidPayError


class salaryEmployee(CommissionEmployee):
    def __init__(self, first_nmae, last_name, nin, sales, rate, base_pay):
        super().__init__(first_nmae, last_name, nin, sales, rate)
        self.base_pay = base_pay

    @property
    def base_pay(self):
        return self.base_pay

    @base_pay.setter
    def base_pay(self, pay):
        if pay < Decimal(0.0):
            raise InvalidPayError("Invalid pay")
        self.base_pay = pay

    def earning(self):
        return self.base_pay + super().earning()

    def __repr__(self):
        return f"{super()._repr_()}\n" \
               f"salary: {self.base_pay}\n" \
               f"salary Earning: {self.earning()}"


izu = salaryEmployee("izu", "mirriam", 472, 10000, 1587, 6.3)
print(izu)
print(salaryEmployee, CommissionEmployee)
print(issubclass(CommissionEmployee, object))
print(isinstance(izu, salaryEmployee))