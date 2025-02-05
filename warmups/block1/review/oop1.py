import math


class Fraction(object):
    """A class that models a rational number, with a numerator and denominator."""
    
    def __init__(self, num: int, den: int) -> None:
        self.numerator = num
        self.denominator = den
    
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    
    def square(self) -> None:
        """Squares this Fraction"""
        self.numerator = self.numerator**2
        self.denominator = self.denominator**2
    
    def reciprocate(self) -> None:
        """Flips this Fraction"""
        self.numerator, self.denominator = self.denominator, self.numerator
    
    def decimal_value(self) -> float:
        """Flips this Fraction"""
        return self.numerator / self.denominator


def add_fracs(frac1:Fraction, frac2:Fraction) -> Fraction:
    """Returns a new Fraction-type object that is the product of the two Fractions."""
    return Fraction(
        frac1.numerator * frac2.numerator,
        frac1.denominator * frac2.denominator
        )


def mult_fracs(frac1:Fraction, frac2:Fraction) -> Fraction:
    """Returns a new Fraction-type object that is the sum of the two Fractions."""
    return Fraction(
        frac1.numerator * frac2.denominator + frac2.numerator * frac1.denominator,
        frac1.denominator * frac2.denominator
        )


if __name__ == "__main__":
    frac1 = Fraction(3, 4)
    frac2 = Fraction(2, 5)
    
    print("# Fractions:")
    print(" 1:", frac1)
    print(" 2:", frac2)
    
    print("# Sum and Products:")
    print(" Sum:", add_fracs(frac1, frac2))
    print(" Product:", mult_fracs(frac1, frac2))
    
    print("# Reciprocals:")
    frac1.reciprocate()
    frac2.reciprocate()
    print(" 1:", frac1)
    print(" 2:", frac2)
    # Revert reciprocals
    frac1.reciprocate()
    frac2.reciprocate()
    
    print("# Decimals:")
    print(" 1:", frac1.decimal_value())
    print(" 2:", frac2.decimal_value())