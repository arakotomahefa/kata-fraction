from kata_fraction import Fraction, sum
import math


def test_can_compare_fractions():
    a = Fraction(3, 2)
    b = Fraction(3, 2)
    assert a == b

def test_should_return_sum_fraction():
    fract_1 = Fraction(3, 2)
    fract_2 = Fraction(3, 5)
    actual = sum(fract_1, fract_2)
    expected = Fraction(21, 10)
    assert actual == expected


def test_should_return_reduced_fraction():
    fract_1 = Fraction(1, 6)
    fract_2 = Fraction(2, 6)
    actual = sum(fract_1, fract_2)
    expected = Fraction(1, 2)
    assert actual == expected
