class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value != 0:
            return self.value / other.value
        else:
            raise ValueError("Деление на ноль")

num1 = Calculator(10)
num2 = Calculator(5)

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2

print(f"Сложение: {sum_result}")
print(f"Вычитание: {sub_result}")
print(f"Умножение: {mul_result}")
print(f"Деление: {div_result}")
