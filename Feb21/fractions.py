class Fraction:
    def __init__(self, numerator, denominator):
        self.__num = numerator
        self.__denom = denominator

    @property
    def numer(self):
        return self.__num

    @property
    def denom(self):
        return self.__denom

    @property
    def decimal(self):
        return round(self.numer/self.denom, 4)

    def __str__(self):
        return f'{self.__num}/{self.__denom}'

    def __add__(self, other):
        total_numer = self.numer * other.denom + other.numer * self.denom
        total_denom = self.denom * other.denom
        return Fraction(total_numer, total_denom)

    def __sub__(self, other):
        total_numer = self.numer * other.denom - other.numer * self.denom
        total_denom = self.denom * other.denom
        return Fraction(total_numer, total_denom)

    def __mul__(self, other):
        total_numer = self.numer * other.numer
        total_denom = self.denom * other.denom
        return Fraction(total_numer, total_denom)

    def __truediv__(self, other):
        total_numer = self.numer * other.denom
        total_denom = self.denom * other.numer
        return Fraction(total_numer, total_denom)

    def __eq__(self, other):
        return self.decimal == other.decimal

    def __lt__(self, other):
        return self.decimal < other.decimal

    def __gt__(self, other):
        return self.decimal > other.decimal

    def __le__(self, other):
        return self.decimal <= other.decimal

    def __ge__(self, other):
        return self.decimal >= other.decimal


two_thirds = Fraction(2, 3)
half = Fraction(1, 2)
two_fourth = Fraction(2, 4)
print(two_thirds)
print(half)

# to test __add__
print(two_thirds + half)
# to test __sub__
print(two_thirds - half)
# to test __mul__
print(two_thirds * half)
# to test __truediv__
print(two_thirds / half)
# to test __eq__
print(two_thirds == half)
print(two_fourth == half)
# to test __lt__
print(two_thirds < half)
# to test __gt__
print(two_thirds > half)
# to test __le__
print(two_thirds <= half)
print(two_fourth <= half)
# to test __ge__
print(two_thirds >= half)
print(two_fourth >= half)