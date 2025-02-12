import math


class Fraction(object):
    """A class that models a rational number, with a numerator and denominator."""
    
    def __init__(self, num: int, den: int) -> None:
        self.numerator = num
        self.denominator = den

    def __add__(self, frac2):
        if type(frac2) != Fraction:
            frac2 = Fraction(*float(frac2).as_integer_ratio())

        return Fraction(
            self.numerator * frac2.denominator + frac2.numerator * self.denominator,
            self.denominator * frac2.denominator
            )

    def __mul__(self, frac2):
        if type(frac2) != Fraction:
            frac2 = Fraction(*float(frac2).as_integer_ratio())

        return Fraction(
            self.numerator * frac2.numerator,
            self.denominator * frac2.denominator
            )

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def square(self) -> None:
        """Squares the denominator and numerator."""
        self.numerator = self.numerator**2
        self.denominator = self.denominator**2

    def reciprocate(self) -> None:
        """Flips the denominator and numerator."""
        self.numerator, self.denominator = self.denominator, self.numerator

    def decimal_value(self) -> float:
        """Returns the decimal value of the fraction."""
        return self.numerator / self.denominator

    def mixed_str(self) -> float:
        """Returns a string representing the mixed fraction form."""
        return f"{self.numerator // self.denominator}|{self.numerator % self.denominator}/{self.denominator}"

    def copy(self):
        """Returns the decimal value of the fraction."""
        return Fraction(self.numerator, self.denominator)

    def reduce(self) -> None:
        """Reduces the fraction."""
        gcd = math.gcd(self.numerator, self.denominator)

        self.denominator //= gcd
        self.numerator //= gcd


def add_fracs(frac1:Fraction, frac2:Fraction) -> Fraction:
    """Returns a new Fraction-type object that is the sum of the two Fractions."""
    return frac1 + frac2


def mult_fracs(frac1:Fraction, frac2:Fraction) -> Fraction:
    """Returns a new Fraction-type object that is the product of the two Fractions."""
    return frac1 * frac2


if __name__ == "__main__":
    frac1 = Fraction(3, 4)
    frac2 = Fraction(2, 5)
    frac3 = Fraction(24, 60)

    print("1. Fractions:")
    print("> 1:", frac1)
    print("> 2:", frac2)

    print("\n2. Sum")
    print("> Sum:", add_fracs(frac1, frac2))

    print("\n3. Product")
    print("> Product:", mult_fracs(frac1, frac2))

    print("\n4. Reciprocals:")
    frac1.reciprocate()
    frac2.reciprocate()
    print("> 1:", frac1)
    print("> 2:", frac2)
    frac1.reciprocate()
    frac2.reciprocate()

    print("\n5. Decimals:")
    print("> 1:", frac1.decimal_value())
    print("> 2:", frac2.decimal_value())

    print("\n6. Mixed form:")
    print("> 1:", frac1.mixed_str())
    print("> 2:", frac2.mixed_str())

    print("\n7. Reduce:")
    print(">", frac3)
    frac3.reduce()
    print(">", frac3) # 2/5

    print("\n8. Copy:")
    print("> Copied 1:", hex(id(frac1.copy())))
    print("> Original 1:", hex(id(frac1)))

    print("\n9. BONUS:")
    print("> +:", (frac1 + 1))
    print("> *:", (frac1 * 1))
