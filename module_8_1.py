from decimal import Decimal
def add_everything_up(a, b):

    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(Decimal('123.456'), Decimal('7'))) # чтобы погрешность убрать

