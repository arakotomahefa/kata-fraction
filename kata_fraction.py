import math


def sum(a, b):
    numerateur = a.numerateur * b.denominateur + b.numerateur * a.denominateur
    denominateur = a.denominateur * b.denominateur
    gcd = math.gcd(numerateur, denominateur)
    return Fraction(numerateur // gcd, denominateur // gcd)


class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def __eq__(self, other):
        return (
            self.numerateur == other.numerateur
            and self.denominateur == other.denominateur
        )
